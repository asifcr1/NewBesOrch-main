from datetime import  datetime
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from datetime import datetime, timedelta
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
import uvicorn
from data.appendData import data_append
import data.datadict as dd
import requests
from data.schema import *
import concurrent.futures
import webhooks
import hashlib
import itertools


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
clientID = "4243edc714a54485b5d63d354164c792"
clientSecret = "MGVmMWE1N2ItYWZiZi00ZDI3LThmZDgtYjk4MDY5ZTBmMDA5"
authorization_url = "https://public-api.ssg-wsg.sg/dp-oauth/oauth/token"

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

def accessToken():
    data = {'grant_type': 'client_credentials'}
    access_token_response = requests.post(authorization_url, data=data, auth=(clientID, clientSecret))
    print(access_token_response.json())
    return access_token_response.json()["access_token"]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# Password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#OAuth 2.0
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

#CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
#Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#Encrypt Password
def get_password_hash(password):
    return pwd_context.hash(password)

#Get User
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

#Authentication
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

#Create Token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#Get Current User
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

#Get Current Active User
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user



@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

def removeDuplicate(data):
    seen = set()
    new_list = []
    for d in data:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            new_list.append(d)
    return new_list


def getCourses():
    data = requests.get("https://0883b980-cb6c-41d6-b4d9-23cebf53b1de.mock.pstmn.io/course/get")
    json_data = data.json().get('data').get('courses')
    return json_data
        
def retrieveCourseRun(runID):
    url = "https://mock-api.ssg-wsg.sg/courses/runs/"+ str(runID)
    access_token = accessToken()
    headers = {"Authorization": f"Bearer {access_token}"}
    course_category_response = requests.get(url, headers=headers)
    dd.data.get("CourseRun").append(course_category_response.json().get("data").get("course")) 
       
#Retrive Course Details by Training Provider UEN Number
@app.get("/beso/course/details")
async def get_course(): 
    courses = getCourses()
    data_append(courses)
    
    return dd.data.get("Course")
         
# Get Course Details by Reference Number
@app.get("/beso/trainingproviders/{uen}/courses")
async def get_course_details(uen: str):
    courses = [d for d in dd.data.get("Course") if d.get("trainingProvider") == uen.replace(' ', '')]
    print(courses)
    if courses:
        contact_person = removeDuplicate([ cper for course in courses if course.get("contactPerson") for cp in course.get("contactPerson") if dd.data.get("ContactPersons") for cper in dd.data.get("ContactPersons") if cper.get("fullName") == cp])
        brochure  = removeDuplicate([bc for course in courses if course.get("brochure") if dd.data.get("Brochure") for bc in dd.data.get("Brochure") if course.get("brochure") == bc])    
        tags = removeDuplicate([t for course in courses if course.get("tags") for tag in [course.get("tags")] if dd.data.get("Tags") for t in dd.data.get("Tags") if t.get("text") == tag])
        # support = [s for course in courses if course.get("referenceNumber") if dd.data.get("Support") for s in dd.data.get("Support") if s.get("referenceNumber") == course.get("referenceNumber")]
        runs = removeDuplicate([r for course in courses if course.get("runs") for run in course.get("runs") if dd.data.get("Runs") for r in dd.data.get("Runs") if r.get("id") == run])
        course_titles = [course.get("title") for course in courses]
        referenceNumbers = [{"uen": uen, "course" : course_titles}]
        print("Contact Person", len(contact_person), "records")
        print("Brochure", len(brochure), "records")
        print("Tags", len(tags), "records")
        print("Runs", len(runs), "records")
        print("Courses", len(courses), "records")
        print("Reference Numbers", referenceNumbers, "records")
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [
                        # executor.submit(webhooks.InsertContactPerson, contact_person),
                        # executor.submit(webhooks.InsertBrochure, brochure),
                        # executor.submit(webhooks.InsertTags, tags),
                        executor.submit(webhooks.InsertRuns, runs),
                    ]
            for f in concurrent.futures.as_completed(results):
                print(f.result())

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(webhooks.InsertCourse, courses)]
            for f in concurrent.futures.as_completed(results):
                print(f.result())
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(webhooks.InsertTrainingProvider, referenceNumbers)]
            for f in concurrent.futures.as_completed(results):
                print(f.result())

        return courses
    else:
        raise HTTPException(status_code=404, detail="No Course Found")
    

#Get Course Run Details by Course Reference Number
@app.get("/course/run/{ref}")
def get_course_run_by_ref(ref: str):    
    #get run id list from db by ref 
    run_list = [course.get("runs") for course in dd.data.get("Course") if course.get("referenceNumber") == ref]
    run_list.sort()
    [mylist] = list(k for k,_ in itertools.groupby(run_list))
    runs = [run for id in mylist for run in dd.data.get("Runs") if run.get("id") == id]
    seen = set()
    new_l = []
    for d in runs:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return new_l
         
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
