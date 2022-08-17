from __future__ import annotations
import re
from typing import Any, Optional
from pydantic import BaseModel, Field, validator
import hashlib

def generateID(string):
    hash_object = hashlib.sha256(string.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig
  

def normalize(data: dict, name: str) -> dict:
    if data is not None:
        for k, v in data.items():
            if k == name:
                return v

def normalize_dict(data: dict, name1: str, name2: str = None) -> dict:
    if data is not None:
        for k, v in data.items():
            if type(v) == dict and k == name1:
                return normalize(v, name2)
            elif type(v) == list and k == name1:
                return normalize_list3(v, name2)
            elif k == name1:
                return v

def normalize_list(data: list, name: str) -> list:
    lists = []
    if data is not None:
        for v in data:
            for k, val in v.items():
                if k == name:
                    if type(val) == dict:
                        lists.append(normalize(val, name))
                    elif type(val) == list:
                        lists.append(normalize_list(val, name))
                    else:
                        lists.append(val)
            if not lists:
                for k, val in v.items():
                    if type(val) == dict:
                        lists.append(normalize(val, name))
    return lists


def normalize_list3(data: list, name: str, n2: str = None, n3: str = None, n4: str =None, n5: str = None) -> list:
    lists = []
    if data is not None:
        for v in data:
            if type(v) == dict:
                for k1, v1 in v.items():
                    if k1 == name:
                        if n2 != None:
                            if type(v1) == dict:
                                lists.append(normalize(v1, n2))
                            elif type(v1) == list:
                                lists.append(normalize_list3(v1, n2))
                        else:
                            lists.append(v1)

            elif type(v) == list:
                for val in v:
                    for k1, v1 in val:
                        if k1 == name:
                            if n2 != None:
                                if type(v1) == dict:
                                    lists.append(normalize(v1, n2))
                                elif type(v1) == list:
                                    lists.append(normalize_list3(v1, n2))
                            else:
                                lists.append(v1)

            else:
                lists.append(v)

        return lists
                                                                            
class Course(BaseModel):
    url : Optional[str]
    createdBy: dict = Field(..., alias="meta")
    updatedBy: dict = Field(..., alias="meta")
    createdDate: dict = Field(..., alias="meta")
    updatedDate: dict = Field(..., alias="meta")
    fees : Optional[list]
    runs : Optional[list]
    tags : Optional[list]
    view : Optional[dict]
    title : Optional[str]
    status : Optional[dict]
    code : Optional[str]
    cluster : Optional[dict]
    content : Optional[str]
    outcome : Optional[dict]
    newFlag : Optional[str]
    quality : Optional[dict]
    sectors : Optional[list]
    seoName : Optional[str]
    brochure : Optional[dict]
    category : Optional[dict]
    jobRoles : Optional[list]
    taggings : Optional[list]
    videoUrl : Optional[str]
    jobLevels : Optional[list]
    objective : Optional[str]
    deleteFlag : Optional[str]
    enquiryUrl : Optional[str]
    isExaminable : Optional[str]
    corporateRun : Optional[list] = Field(..., alias="runs")
    feeSubsidy : Optional[int]
    description : Optional[str]
    disbursedTo : Optional[str]
    facultyName : Optional[str]
    initiatives : Optional[str]
    popularFlag : Optional[str]
    redirectUrl : Optional[str]
    featuredFlag : Optional[str]
    masterSource : Optional[str]
    contactPerson : Optional[list]
    wsqFrameworks : Optional[list]
    specialisation : Optional[str]
    areaOfTrainings : Optional[list]
    eduOfTargetAuds : Optional[list]
    fieldOfStudies1 : Optional[list]
    fieldOfStudies2 : Optional[list]
    modeOfTrainings : Optional[list]
    isPETOrganization : Optional[str]
    referenceNumber : Optional[str]
    registrationUrl : Optional[str]
    displayImageName : Optional[str]
    entryRequirement : Optional[str]
    skillsFrameworks : Optional[list]
    trainingProvider : Optional[dict]
    statisticsSummary : Optional[dict]
    methodOfDeliveries : Optional[list]
    locationOfTrainings : Optional[list]
    numberOfTrainingDay : Optional[str]
    redirectRegisterUrl : Optional[str]
    mediumOfInstructions : Optional[list]
    targetTrainingGroups : Optional[list]
    qualificationAttained : Optional[dict]
    trainingProviderAlias : Optional[str]
    lengthOfCourseDuration : Optional[str]
    publicFundingIndicator : Optional[dict]
    isShownCourseDescription : Optional[str]
    targetWorkforceSegment : Optional[dict]
    externalReferenceNumber : Optional[str]
    totalTrainingDurationHour : Optional[str]
    minimumEducationRequirements : Optional[dict]
    skillsConnectReferenceNumber : Optional[str]
    totalCostOfTrainingPerTrainee : Optional[str]
    skillsFutureCreditReferenceNumber : Optional[str]
    support : Optional[list]
    statisticsCourseReferenceNumber : Optional[dict] = Field(..., alias="statisticsSummary")
    statisticsPageViewCount: Optional[dict] = Field(..., alias="statisticsSummary")

    @validator('statisticsCourseReferenceNumber')
    def statisticsCourseReferenceNumber_validator(cls, v):
        return normalize(v, "courseReferenceNumber")

    @validator('statisticsPageViewCount')
    def statisticsPageViewCount_validator(cls, v):
        return normalize(v, "pageViewCount")
    
    @validator("fees")
    def validate_fees(cls,v):
        if v is not None and v != []:
                return normalize_list3(v, "id")[0]

    @validator("runs")
    def validate_runs(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "id")

    @validator("corporateRun")
    def validator_corporateRun(cls, v):
        if v != None:
            if v is not None and v != []:
                return "Yes"
        else:
            if v is not None and v != []:
                return "No"
        
    @validator("tags")
    def validate_tags(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "text")[0]

    @validator("outcome")
    def validate_outcome(cls, v):
        if v is not None and v != []:
            return normalize_dict(v, "overallOutcome", "average")

    @validator("view")
    def validate_view(cls, v):
        if v is not None and v != []:
            return str(normalize_dict(v, "code")) + " - " + normalize_dict(v, "description")
    
    @validator("status")
    def validate_status(cls, v):
        if v is not None and v != []:
            return str(normalize_dict(v, "code")) + " - " + normalize_dict(v, "description")

    @validator("cluster")
    def validate_cluster(cls, v):
        codes = normalize_list3(v, "code")
        descriptions = normalize_list3(v, "description")
        if v is not None and v != []:
                return [str(code) + " - " + description for code, description in zip(codes, descriptions)]

    @validator("support")
    def validate_support(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "category")

    @validator("jobLevels")
    def validate_jobLevels(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]
    
    @validator("quality")
    def validate_quality(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallQuality", "average")
    
    @validator("sectors")
    def validate_sectors(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]

    @validator("brochure")
    def validate_brochure(cls, v):
        if v is not None and v != []:
                return normalize(v, "id")

    @validator("category")
    def validate_category(cls, v):
        if v is not None and v != []:
            return str(normalize_dict(v, "code")) + " - " + normalize_dict(v, "description")
    
            
    @validator("jobRoles")
    def validate_jobRoles(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "title")[0]
    
    @validator("taggings")
    def validate_taggings(cls, v):
        if v is not None and v != []:
                return str(normalize_list3(v, "code")[0]) + " - "+ normalize_list3(v, "description")[0]


    @validator("contactPerson")
    def validate_contactPerson(cls, v):
        if v is not None and v != []:
            # names = normalize_list3(v, "code")
            return normalize_list3(v, "fullName")

    @validator("wsqFrameworks")
    def validate_wsqFrameworks(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "wsqFrameworkDescription")

    @validator("areaOfTrainings")
    def validate_areaOfTrainings(cls, v):
        if v is not None and v != []:
                return str(normalize_list3(v, "code")[0]) + " - "+ normalize_list3(v, "description")[0]
    
    @validator("eduOfTargetAuds")
    def validate_eduOfTargetAuds(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code") 
    
    @validator("fieldOfStudies1")
    def validate_fieldOfStudies1(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code") 
    
    @validator("fieldOfStudies2")
    def validate_fieldOfStudies2(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")
    
    
    
    @validator("modeOfTrainings")
    def validate_modeOfTrainings(cls, v):
        if v is not None and v != []:
            return str(normalize_list3(v, "code")[0]) + " - "+ normalize_list3(v, "description")[0]

    @validator("skillsFrameworks")
    def validate_skillsFrameworks(cls, v):
        if v is not None and v != []:
            return normalize_list3(v, "subSectors", "name")

    @validator("trainingProvider")
    def validate_trainingProvider(cls, v):
        if v is not None and v != []:
            return normalize(v, "uen")

    @validator("statisticsSummary")
    def validate_foreignAddress(cls, v):
        if v is not None and v != []:
                return normalize(v, "pageViewCount")
    
    @validator("methodOfDeliveries")
    def validate_methodOfDeliveries(cls, v):
        if v is not None and v != []:
                return str(normalize_list3(v, "code")[0]) + " - "+ normalize_list3(v, "description")[0]

    @validator("locationOfTrainings")
    def validate_locationOfTrainings(cls, v):
        if v is not None and v != []:
            codes = normalize_list3(v, "code")
            descriptions = normalize_list3(v, "description")
            return [str(code) + " - " + str(description) for code, description in zip(codes, descriptions)]

    @validator("mediumOfInstructions")
    def validate_mediumOfInstructions(cls, v):
        if v is not None and v != []:
            codes = normalize_list3(v, "code")
            descriptions = normalize_list3(v, "description")
            return [str(code) + " - " + str(description) for code, description in zip(codes, descriptions)]

    @validator("targetTrainingGroups")
    def validate_targetTrainingGroups(cls, v):
        codes = normalize_list3(v, "code")
        descriptions = normalize_list3(v, "description")
        if v is not None and v != []:
                return [str(code) + " - " + description for code, description in zip(codes, descriptions)]

    @validator("qualificationAttained")
    def validate_qualificationAttained(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "description")

    @validator("publicFundingIndicator")
    def validate_publicFundingIndicator(cls, v):
        if v is not None and v != [] and v != {}:
                return str(normalize_dict(v, "code")) + " - " + normalize_dict(v, "description")

    @validator("targetWorkforceSegment")
    def validate_targetWorkforceSegment(cls, v):
        if v is not None and v != [] and v !={}:
                return str(normalize_dict(v, "code")) + " - " + normalize_dict(v, "description")

    @validator("minimumEducationRequirements")
    def validate_minimumEducationRequirements(cls, v):
        if v is not None and v != [] and v!={}:
                return str(normalize_dict(v, "code")) + " - "+ normalize_dict(v, "description")

    @validator("createdBy")
    def validate_createdBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updatedBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createdDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updatedDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class Fees(BaseModel):
    id : Optional[int] 
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
    feeType : Optional[str] 
    feeUpdateDate : Optional[int] 
    feeTypeEffectiveDate : Optional[int] 

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_list3(v, "meta", "createBy")[0]
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "updateDate")

class Runs(BaseModel):
    id: Optional[int] 
    # createdBy : Optional[dict] = Field(..., alias='meta')
    # updatedBy : Optional[dict] = Field(..., alias='meta')
    # createdDate : Optional[dict] = Field(..., alias='meta')
    # updatedDate : Optional[dict] = Field(..., alias='meta')
    room: Optional[str] 
    unit: Optional[str] 
    block: Optional[str] 
    floor: Optional[str] 
    street: Optional[str] 
    # deleted: Optional[list] 
    building: Optional[str] 
    intakeSize: Optional[int] 
    postalCode: Optional[str] 
    scheduleInfo: Optional[str] 
    courseEndDate: Optional[int] 
    courseVacancy: Optional[dict] 
    modeOfTraining: Optional[str] 
    courseStartDate: Optional[int] 
    organizationKey: Optional[str] 
    referenceNumber: Optional[str]  
    courseAdminEmail: Optional[str] 
    scheduleInfoType: Optional[dict] 
    wheelChairAccess: Optional[str] 
    registrationClosingDate: Optional[int] 
    registrationOpeningDate: Optional[int] 
    
    @validator("courseVacancy")
    def validate_courseVacancy(cls, v):
        if v is not None and v != []:
            return normalize_dict(v, "code") + " - " + normalize_dict(v, "description")

    @validator("scheduleInfoType")
    def validate_scheduleInfoType(cls, v):
        if v is not None and v != []:
            return normalize_dict(v, "code") + " - " + normalize_dict(v, "description")
    # @validator("createdBy")
    # def validate_createBy(cls, v):
    #         if v is not None and v != []:
    #             return normalize(v, "createBy")
        
    # @validator("updatedBy")
    # def validate_updateBy(cls, v):
    #         if v is not None and v != []:
    #             return normalize(v, "updateBy")

    # @validator("createdDate")
    # def validate_createDate(cls, v):
    #         if v is not None and v != []:
    #             return normalize(v, "createDate")

    # @validator("updatedDate")
    # def validate_updateDate(cls, v):
    #         if v is not None and v != []:
    #             return normalize(v, "updateDate")

class ScheduleInfoType(BaseModel):
    code : Optional[list] = Field(..., alias='runs')
    description : Optional[list] = Field(..., alias='runs')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
    


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "scheduleInfoType", "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "scheduleInfoType", "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class CourseVacancy(BaseModel):
    code : Optional[list] = Field(..., alias='runs')
    description : Optional[list] = Field(..., alias='runs')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "courseVacancy", "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "courseVacancy", "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class Meta(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
    
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class Tags(BaseModel):
    text : Optional[str]
    count : Optional[int]
    nettfee : Optional[int]

class View(BaseModel):
    code : Optional[dict] = Field(..., alias='view')
    description : Optional[dict] = Field(..., alias='view')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
 

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")
        
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")
            

class Status(BaseModel):
    code : Optional[dict] = Field(..., alias='status')
    description : Optional[dict] = Field(..., alias='status')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
    
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")
            

class Cluster(BaseModel):
    code : Optional[dict] = Field(..., alias='cluster')
    description : Optional[dict] = Field(..., alias='cluster')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
 

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
    
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class Outcome(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='outcome')
    updatedBy : Optional[dict] = Field(..., alias='outcome')
    createdDate : Optional[dict] = Field(..., alias='outcome')
    updatedDate : Optional[dict] = Field(..., alias='outcome')
    overallOutcome : Optional[dict] = Field(..., alias='outcome')
    expandedJobScope : Optional[dict] = Field(..., alias='outcome')
    ableToApplyLearning : Optional[dict] = Field(..., alias='outcome')
    numberOfRespondents : Optional[dict] = Field(..., alias='outcome')
    betterJobPerformance : Optional[dict] = Field(..., alias='outcome')


    @validator("overallOutcome")
    def validate_overallOutcome(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallOutcome", "average")

    @validator("expandedJobScope")
    def validate_expandedJobScope(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "expandedJobScope", "average")

    @validator("ableToApplyLearning")
    def validate_ableToApplyLearning(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ableToApplyLearning", "average")

    @validator("numberOfRespondents")
    def validate_numberOfRespondents(cls, v):
        if v is not None and v != []:
                return normalize(v, "numberOfRespondents")
    
    @validator("betterJobPerformance")
    def validate_betterJobPerformance(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "betterJobPerformance", "average")

    @validator("createdBy")
    def validate_createdBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updatedBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createdDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updatedDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")


class OverallOutcome(BaseModel):
    average : Optional[dict] = Field(..., alias='outcome')
    starsRating : Optional[dict] = Field(..., alias='outcome')
    createdBy : Optional[dict] = Field(..., alias='outcome')
    updatedBy : Optional[dict] = Field(..., alias='outcome')
    createdDate : Optional[dict] = Field(..., alias='outcome')
    updatedDate : Optional[dict] = Field(..., alias='outcome')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallOutcome", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallOutcome", "starsRating")
        

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class ExpandedJobScope(BaseModel):
    average : Optional[dict] = Field(..., alias='outcome')
    starsRating : Optional[dict] = Field(..., alias='outcome')
    createdBy : Optional[dict] = Field(..., alias='outcome')
    updatedBy : Optional[dict] = Field(..., alias='outcome')
    createdDate : Optional[dict] = Field(..., alias='outcome')
    updatedDate : Optional[dict] = Field(..., alias='outcome')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "expandedJobScope", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "expandedJobScope", "starsRating")
        

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class BetterJobPerformance(BaseModel):
    average : Optional[dict] = Field(..., alias='outcome')
    starsRating : Optional[dict] = Field(..., alias='outcome')
    createdBy : Optional[dict] = Field(..., alias='outcome')
    updatedBy : Optional[dict] = Field(..., alias='outcome')
    createdDate : Optional[dict] = Field(..., alias='outcome')
    updatedDate : Optional[dict] = Field(..., alias='outcome')

    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "betterJobPerformance", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "betterJobPerformance", "starsRating")
        

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")


class AbleToApplyLearning(BaseModel):
    average : Optional[dict] = Field(..., alias='outcome')
    starsRating : Optional[dict] = Field(..., alias='outcome')
    createdBy : Optional[dict] = Field(..., alias='outcome')
    updatedBy : Optional[dict] = Field(..., alias='outcome')
    createdDate : Optional[dict] = Field(..., alias='outcome')
    updatedDate : Optional[dict] = Field(..., alias='outcome')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ableToApplyLearning", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ableToApplyLearning", "starsRating")
        

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class Quality(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='quality')
    updatedBy : Optional[dict] = Field(..., alias='quality')
    createdDate : Optional[dict] = Field(..., alias='quality')
    updatedDate : Optional[dict] = Field(..., alias='quality')
    learning : Optional[dict] = Field(..., alias='quality')
    overallQuality : Optional[dict] = Field(..., alias='quality')
    customerService : Optional[dict] = Field(..., alias='quality')
    numberOfRespondents : Optional[dict] = Field(..., alias='quality')
    trainerCourseContent : Optional[dict] = Field(..., alias='quality')


    @validator("learning")
    def validate_learning(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "learning", "average")

    @validator("overallQuality")
    def validate_overallQuality(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallQuality", "average")
     
    @validator("customerService")
    def validate_customerService(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "customerService", "average")
     
    @validator("numberOfRespondents")
    def validate_numberOfRespondents(cls, v):
        if v is not None and v != []:
                return normalize(v, "numberOfRespondents")
    
    @validator("trainerCourseContent")
    def validate_trainerCourseContent(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "trainerCourseContent", "average")
     
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class OverallQuality(BaseModel):
    average : Optional[dict] = Field(..., alias='quality')
    starsRating : Optional[dict] = Field(..., alias='quality')
    createdBy : Optional[dict] = Field(..., alias='quality')
    updatedBy : Optional[dict] = Field(..., alias='quality')
    createdDate : Optional[dict] = Field(..., alias='quality')
    updatedDate : Optional[dict] = Field(..., alias='quality')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallQuality", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "overallQuality", "starsRating")
        

    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class Learning(BaseModel):
    average : Optional[dict] = Field(..., alias='quality')
    starsRating : Optional[dict] = Field(..., alias='quality')
    createdBy : Optional[dict] = Field(..., alias='quality')
    updatedBy : Optional[dict] = Field(..., alias='quality')
    createdDate : Optional[dict] = Field(..., alias='quality')
    updatedDate : Optional[dict] = Field(..., alias='quality')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "learning", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "learning", "starsRating")
        
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class CustomerService(BaseModel):
    average : Optional[dict] = Field(..., alias='quality')
    starsRating : Optional[dict] = Field(..., alias='quality')
    createdBy : Optional[dict] = Field(..., alias='quality')
    updatedBy : Optional[dict] = Field(..., alias='quality')
    createdDate : Optional[dict] = Field(..., alias='quality')
    updatedDate : Optional[dict] = Field(..., alias='quality')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "customerService", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "customerService", "starsRating")
        
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class TrainerCourseContent(BaseModel):
    average : Optional[dict] = Field(..., alias='quality')
    starsRating : Optional[dict] = Field(..., alias='quality')
    createdBy : Optional[dict] = Field(..., alias='quality')
    updatedBy : Optional[dict] = Field(..., alias='quality')
    createdDate : Optional[dict] = Field(..., alias='quality')
    updatedDate : Optional[dict] = Field(..., alias='quality')


    @validator("average")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "trainerCourseContent", "average")
    
    @validator("starsRating")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "trainerCourseContent", "starsRating")
        
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class Sectors(BaseModel):
    code : Optional[list] = Field(..., alias='sectors')
    description : Optional[list] = Field(..., alias='sectors')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list(v, "code")[0]
    
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class Support(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
    period : Optional[dict] 
    deleted : Optional[str] 
    support : Optional[dict] 
    category : Optional[str] 
    detailsId : Optional[int] 
    effectiveDate : Optional[int] 
    referenceNumber : Optional[str] 


    @validator("period")
    def validate_period(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "taggingCode")
    
    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "updateDate")
    
    
    
class Period(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
    startDate : Optional[dict]
    endDate: Optional[dict] 
    taggingCode : Optional[int]
    taggingDescription : Optional[dict]

    @validator("startDate")
    def validate_startDate(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "period", "to")[0]

    @validator("endDate")
    def validate_endDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "period", "to")[0]

    @validator("taggingCode")
    def validate_taggingCode(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "period", "taggingCode")[0]
    
    @validator("taggingDescription")
    def validate_taggingDescription(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "period", "taggingDescription")[0]
    
    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "updateDate")
    
class Brochure(BaseModel):
    id : Optional[dict] = Field(..., alias='brochure')
    url : Optional[dict] = Field(..., alias='brochure')
    name : Optional[dict] = Field(..., alias='brochure')
    organizationKey : Optional[dict] = Field(..., alias='brochure')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("id")
    def validate_id(cls, v):
        if v is not None and v != []:
                return normalize(v, "id")
        
    @validator("url")
    def validate_url(cls, v):
        if v is not None and v != []:
                return normalize(v, "url")

    @validator("name")
    def validate_name(cls, v):
        if v is not None and v != []:
                return normalize(v, "name")

    @validator("organizationKey")
    def validate_organizationKey(cls, v):
        if v is not None and v != []:
                return normalize(v, "organizationKey")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class Category(BaseModel):
    code : Optional[dict] = Field(..., alias='category')
    description : Optional[dict] = Field(..., alias='category')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")
    

class JobRoles(BaseModel):
    code : Optional[list] = Field(..., alias='jobRoles')
    title : Optional[list] = Field(..., alias='jobRoles')
    typeId : Optional[list] = Field(..., alias='jobRoles')
    sectorUri : Optional[list] = Field(..., alias='jobRoles')
    jobRoleUri : Optional[list] = Field(..., alias='jobRoles')
    sectorCode : Optional[list] = Field(..., alias='jobRoles')
    salaryRange : Optional[list] = Field(..., alias='jobRoles')
    sectorDescription : Optional[list] = Field(..., alias='jobRoles')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]
        
    @validator("title")
    def validate_title(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "title")[0]
    
    @validator("typeId")
    def validate_typeId(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "typeId")[0]

    @validator("sectorUri")
    def validate_sectorUri(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "sectorUri")[0]

    @validator("jobRoleUri")
    def validate_jobRoleUri(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "jobRoleUri")[0]

    @validator("sectorCode")
    def validate_sectorCode(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "sectorCode")[0]

    @validator("salaryRange")
    def validate_salaryRange(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "salaryRange")[0]

    @validator("sectorDescription")
    def validate_sectorDescription(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "sectorDescription")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")
    
class Taggings(BaseModel):
    code : Optional[list] = Field(..., alias='taggings')
    description : Optional[list] = Field(..., alias='taggings')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]
        
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class JobLevels(BaseModel):
    code : Optional[list] = Field(..., alias='jobLevels')
    description : Optional[list] = Field(..., alias='jobLevels')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]
        
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class ContactPersons(BaseModel):
    id : Optional[str] 
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
    role : Optional[str] 
    email : Optional[dict]
    fullName : Optional[str] 
    telephone : Optional[dict]
    salutation : Optional[str] 
    designation : Optional[str]
    officeNumber : Optional[str]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "createBy")

    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "updateDate")


    @validator("email")
    def validate_email(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "full")

    @validator("telephone")
    def validate_telephone(cls, v):
        if v is not None and v != []:
                return str(normalize_dict(v,  "countryCode")) + str(normalize_dict(v,  "areaCode")) + str(normalize_dict(v,  "number"))

class ContactPersonEmail(BaseModel):
    full : Optional[list] = Field(..., alias='contactPerson')
    atSign : Optional[list] = Field(..., alias='contactPerson')
    domain : Optional[list] = Field(..., alias='contactPerson')
    localPart : Optional[list] = Field(..., alias='contactPerson')
    createdBy : Optional[list] = Field(..., alias='contactPerson')
    updatedBy : Optional[list] = Field(..., alias='contactPerson')
    createdDate : Optional[list] = Field(..., alias='contactPerson')
    updatedDate : Optional[list] = Field(..., alias='contactPerson')


    @validator("full")
    def validate_full(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "email", "full")[0]

    @validator("atSign")
    def validate_atSign(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "email", "atSign")[0]

    @validator("domain")
    def validate_domain(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "email", "domain")[0]

    @validator("localPart")
    def validate_localPart(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "email", "localPart")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "meta", "createBy")[0]

    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"meta", "updateBy")[0]

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "meta","createDate")[0]

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"meta", "updateDate")[0]

class ContactPersonTelePhone(BaseModel):
    number : Optional[list] = Field(..., alias='contactPerson')
    areaCode : Optional[list] = Field(..., alias='contactPerson')
    countryCode : Optional[list] = Field(..., alias='contactPerson')
    internationalPrefix : Optional[list] = Field(..., alias='contactPerson')
    createdBy : Optional[list] = Field(..., alias='contactPerson')
    updatedBy : Optional[list] = Field(..., alias='contactPerson')
    createdDate : Optional[list] = Field(..., alias='contactPerson')
    updatedDate : Optional[list] = Field(..., alias='contactPerson')


    @validator('number')
    def check_number(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, 'telephone', "number")

    @validator('areaCode')
    def check_areaCode(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, 'telephone', "areaCode")

    @validator('countryCode')
    def check_countryCode(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, 'telephone', "countryCode")

    @validator('internationalPrefix')
    def check_internationalPrefix(cls, v):
        if v is not None and v != []:
                return  normalize_list3(v, 'telephone', "internationalPrefix")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "meta", "createBy")[0]

    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"meta", "updateBy")[0]

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "meta","createDate")[0]

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"meta", "updateDate")[0]

class WsqFrameworks(BaseModel):
    wsqFrameworkCode : Optional[list] = Field(..., alias='wsqFrameworks')
    competencyStandardCode : Optional[list] = Field(..., alias='wsqFrameworks')
    wsqFrameworkDescription : Optional[list] = Field(..., alias='wsqFrameworks')
    competencyStandardDescription : Optional[list] = Field(..., alias='wsqFrameworks')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")


    @validator("wsqFrameworkCode")
    def validate_wsqFrameworkCode(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "wsqFrameworkCode")[0]

    @validator("competencyStandardCode")
    def validate_competencyStandardCode(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "competencyStandardCode")[0]

    @validator("wsqFrameworkDescription")
    def validate_wsqFrameworkDescription(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "wsqFrameworkDescription")[0]

    @validator("competencyStandardDescription")
    def validate_competencyStandardDescription(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "competencyStandardDescription")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class AreaOfTraining(BaseModel):
    code : Optional[list] = Field(..., alias='areaOfTrainings')
    description : Optional[list] = Field(..., alias='areaOfTrainings')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class EduOfTargetAuds(BaseModel):
    code : Optional[list] = Field(..., alias='eduOfTargetAuds')
    description : Optional[list] = Field(..., alias='eduOfTargetAuds')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class FieldOfStudies1(BaseModel):
    code : Optional[list] = Field(..., alias='fieldOfStudies1')
    description : Optional[list] = Field(..., alias='fieldOfStudies1')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")

        
    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != [] and v != []:
                return normalize_list(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != [] and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")
class FieldOfStudies2(BaseModel):
    code : Optional[list] = Field(..., alias='fieldOfStudies2')
    description : Optional[list] = Field(..., alias='fieldOfStudies2')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != [] and v != []:
                return normalize_list3(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != [] and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class ModeOfTrainings(BaseModel):
    code : Optional[list] = Field(..., alias='modeOfTrainings')
    description : Optional[list] = Field(..., alias='modeOfTrainings')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta")

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]

    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class SkillsFrameworks(BaseModel):
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 
    sectorCode : Optional[list] = Field(..., alias='skillsFrameworks')
    sectorName : Optional[list] = Field(..., alias='skillsFrameworks')
    subSectors : Optional[list] = Field(..., alias='skillsFrameworks')
    mappedSkillsCompetency : Optional[list] = Field(..., alias='skillsFrameworks')

    @validator("sectorCode")
    def check_sector_code(cls, v):
        if v is not None and v != []:
                return normalize_list(v, "sectorCode")[0]

    @validator("sectorName")
    def check_sector_name(cls, v):
        if v is not None and v != []:
                return normalize_list(v, "sectorName")[0]
    
    @validator("subSectors")
    def validate_subSectors(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "name")[0]

    @validator("mappedSkillsCompetency")
    def validate_mappedSkillsCompetency(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency", "generic", "title")[0][0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class SubSectors(BaseModel):
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 
    name : Optional[list] = Field(..., alias='skillsFrameworks')
    tracks : Optional[list] = Field(..., alias='skillsFrameworks')

    @validator("name")
    def check_name(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "name")[0]

    @validator("tracks")
    def validate_occupations(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "tracks", "name")[0][0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class Tracks(BaseModel):
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 
    name : Optional[list] = Field(..., alias='skillsFrameworks')
    occupations : Optional[list] = Field(..., alias='skillsFrameworks')


    @validator("name")
    def check_name(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "tracks", "name")[0]
    
    @validator("occupations")
    def validate_occupations(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"subSectors", "tracks", "occupations", "name" )[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class Occupations(BaseModel):
    name : Optional[list] = Field(..., alias="skillsFrameworks")
    jobRoles: Optional[list] = Field(..., alias="skillsFrameworks")
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 


    @validator("name")
    def validate_name(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "tracks", "occupations", "name")[0]

    @validator("jobRoles")
    def validate_jobRoles(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "tracks", "occupations", "jobRoles" , "title")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")


class SkillsFrameworksJobRoles(BaseModel):
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 
    title : Optional[list] = Field(..., alias='skillsFrameworks')
    ILPCode : Optional[list] = Field(..., alias='skillsFrameworks')

    @validator("title")
    def validate_occupations(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "tracks", "occupations", "jobRoles", "title")[0]

    @validator("ILPCode")
    def validate_ILPCode(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "subSectors", "tracks", "occupations", "jobRoles", "ILPCode")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class MappedSkillsCompetency(BaseModel):
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 
    generic : Optional[list] = Field(..., alias='skillsFrameworks')
    keyTask : Optional[list] = Field(..., alias='skillsFrameworks')
    technical : Optional[list] = Field(..., alias='skillsFrameworks')


    @validator('generic')
    def validate_generic(cls, v):
            if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency", "generic", "title")[0][0]
    
    @validator('keyTask')
    def validate_keyTask(cls, v):
            if v is not None and v != []:
                return normalize_list3(v,"mappedSkillsCompetency", "keyTask", "title")[0][0]

    @validator('technical')
    def validate_technical(cls, v):
            if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency", "technical", "title")[0][0]
    
    @validator("createdBy")
    def validate_createBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
            if v is not None and v != []:
                return normalize(v, "updateDate")

class Technical(BaseModel):
    title : Optional[list] = Field(..., alias='skillsFrameworks')
    category : Optional[list] = Field(..., alias='skillsFrameworks')
    proficiencyLevel : Optional[list] = Field(..., alias='skillsFrameworks')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 

    @validator("title")
    def validate_title(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"mappedSkillsCompetency" , "technical", "title")[0]

    @validator("category")
    def validate_category(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency", "technical", "category")[0]

    @validator("proficiencyLevel")
    def validate_proficiencyLevel(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency","technical", "proficiencyLevel")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class KeyTask(BaseModel):
    title : Optional[list] = Field(..., alias='skillsFrameworks')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 


    @validator("title")
    def validate_title(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency", "keyTask", "title")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class Generic(BaseModel):
    title : Optional[list] = Field(..., alias='skillsFrameworks')
    proficiencyLevel : Optional[list] = Field(..., alias='skillsFrameworks')
    createdBy: Optional[dict] = Field(..., alias="meta")
    updatedBy: Optional[dict] = Field(..., alias="meta")
    createdDate: Optional[dict] = Field(..., alias="meta")
    updatedDate: Optional[dict] = Field(..., alias="meta") 

    @validator("title")
    def validate_title(cls, v):
        if v is not None and v != []:
                return normalize_list3(v,"mappedSkillsCompetency", "generic", "title")[0]

    @validator("proficiencyLevel")
    def validate_proficiencyLevel(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "mappedSkillsCompetency", "generic", "proficiencyLevel")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class TrainingProvider(BaseModel):
    uen : Optional[dict] = Field(..., alias='trainingProvider')
    code : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    name : Optional[dict] = Field(..., alias='trainingProvider')
    ssicprimary : Optional[dict] = Field(..., alias='trainingProvider')
    ssicsecondary : Optional[dict] = Field(..., alias='trainingProvider')
    type : Optional[dict] = Field(..., alias='trainingProvider')
    email : Optional[dict] = Field(..., alias='trainingProvider')
    value : Optional[dict] = Field(..., alias='trainingProvider')
    active : Optional[dict] = Field(..., alias='trainingProvider')
    vision : Optional[dict] = Field(..., alias='trainingProvider')
    aboutUs : Optional[dict] = Field(..., alias='trainingProvider')
    address : Optional[dict] = Field(..., alias='trainingProvider')
    deleted : Optional[dict] = Field(..., alias='trainingProvider')
    mission : Optional[dict] = Field(..., alias='trainingProvider')
    outcome : Optional[dict] = Field(..., alias='trainingProvider')
    quality : Optional[dict] = Field(..., alias='trainingProvider')
    thirdParty : Optional[dict] = Field(..., alias='trainingProvider')
    tripartite : Optional[dict] = Field(..., alias='trainingProvider')
    websiteUrl : Optional[dict] = Field(..., alias='trainingProvider')
    brandmessage : Optional[dict] = Field(..., alias='trainingProvider')
    logoFilename : Optional[dict] = Field(..., alias='trainingProvider')
    notification : Optional[dict] = Field(..., alias='trainingProvider')
    contactNumber : Optional[dict] = Field(..., alias='trainingProvider')
    bannerFilename : Optional[dict] = Field(..., alias='trainingProvider')
    foreignAddress : Optional[dict] = Field(..., alias='trainingProvider')
    socialMediaURL : Optional[dict] = Field(..., alias='trainingProvider')
    numberOfEmployees : Optional[dict] = Field(..., alias='trainingProvider')
    yearOfEstablishment : Optional[dict] = Field(..., alias='trainingProvider')
    employerBrandMessage : Optional[dict] = Field(..., alias='trainingProvider')
    emailSubscriptionCode : Optional[dict] = Field(..., alias='trainingProvider')
    acraRegistrationStatus : Optional[dict] = Field(..., alias='trainingProvider')
    supportingGovermentAgency : Optional[dict] = Field(..., alias='trainingProvider')
    registrationTypeDescription : Optional[dict] = Field(..., alias='trainingProvider')
    employmentAgencyLicenseNumber : Optional[dict] = Field(..., alias='trainingProvider')
    view : Optional[dict] = Field(..., alias='trainingProvider') 
    referenceNumber: Optional[str]
    trainingProviderAlias : Optional[str]

    
    @validator("uen")
    def validate_uen(cls, v):
        if v is not None and v != []:
                return normalize(v, "uen")
    
    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
    
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v,"meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

    @validator("name")
    def validate_name(cls, v):
        if v is not None and v != []:
                return normalize(v, "name")

    @validator("ssicprimary")
    def validate_ssicprimary(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ssic", "primaryCode")

    @validator("ssicsecondary")
    def validate_ssicsecondary(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ssic", "secondaryCode")

    @validator("type")
    def validate_type(cls, v):
        if v is not None and v != []:
                return normalize(v, "trainingProviderType")

    @validator("email")
    def validate_email(cls, v):
        if v is not None and v != []:
                return normalize(v, "email")

    @validator("value")
    def validate_value(cls, v):
        if v is not None and v != []:
                return normalize(v, "value")

    @validator("active")
    def validate_active(cls, v):
        if v is not None and v != []:
                return normalize(v, "isActive")

    @validator("vision")
    def validate_vision(cls, v):
        if v is not None and v != []:
                return normalize(v, "vision")

    @validator("aboutUs")
    def validate_aboutUs(cls, v):
        if v is not None and v != []:
                return normalize(v, "aboutUs")

    @validator("address")
    def validate_address(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "id")[0]

    @validator("deleted")
    def validate_deleted(cls, v):
        if v is not None and v != []:
                return normalize(v, "isDeleted")

    @validator("mission")
    def validate_mission(cls, v):
        if v is not None and v != []:
                return normalize(v, "mission")

    @validator("outcome")
    def validate_outcome(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "overallOutcome"), "average")

    @validator("quality")
    def validate_quality(cls, v):
        normalize(normalize_dict(v, "quality", "overallQuality"), "average")


    @validator("notification")
    def validate_notification(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "notification", "applicationReceived")

    @validator("contactNumber")
    def validate_contactNumber(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "contactNumber", "id")[0]
    
    @validator("foreignAddress")
    def validate_foreignAddress(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress", "id")

    @validator("socialMediaURL")
    def validate_socialMediaURL(cls, v):
        if v is not None and v != []:
                return normalize(v, "socialMediaURL")

    @validator("thirdParty")
    def validate_thirdParty(cls, v):
        if v is not None and v != []:
                return normalize(v, "is3rdParty")

    @validator("tripartite")
    def validate_tripartite(cls, v):
        if v is not None and v != []:
                return normalize(v, "isTripartite")

    @validator("websiteUrl")
    def validate_websiteUrl(cls, v):
        if v is not None and v != []:
                return normalize(v, "websiteUrl")

    @validator("brandmessage")
    def validate_brandmessage(cls, v):
        if v is not None and v != []:
                return normalize(v, "brandmessage")

    @validator("logoFilename")
    def validate_logoFilename(cls, v):
        if v is not None and v != []:
                return normalize(v, "logoFilename")

    @validator("bannerFilename")
    def validate_bannerFilename(cls, v):
        if v is not None and v != []:
                return normalize(v, "bannerFilename")

    @validator("numberOfEmployees")
    def validate_numberOfEmployees(cls, v):
        if v is not None and v != []:
                return normalize(v, "numberOfEmployees")

    @validator("yearOfEstablishment")
    def validate_yearOfEstablishment(cls, v):
        if v is not None and v != []:
                return normalize(v, "yearOfEstablishment")

    @validator("employerBrandMessage")
    def validate_employerBrandMessage(cls, v):
        if v is not None and v != []:
                return normalize(v, "employerBrandMessage")

    @validator("emailSubscriptionCode")
    def validate_emailSubscriptionCode(cls, v):
        if v is not None and v != []:
                return normalize(v, "emailSubscriptionCode")
    
    @validator("acraRegistrationStatus")
    def validate_acraRegistrationStatus(cls, v):
        if v is not None and v != []:
                return normalize(v, "acraRegistrationStatus")

    @validator("supportingGovermentAgency")
    def validate_supportingGovermentAgency(cls, v):
        if v is not None and v != []:
                return normalize(v, "supportingGovermentAgency")

    @validator("registrationTypeDescription")
    def validate_registrationTypeDescription(cls, v):
        if v is not None and v != []:
                return normalize(v, "registrationTypeDescription")

    @validator("employmentAgencyLicenseNumber")
    def validate_employmentAgencyLicenseNumber(cls, v):
        if v is not None and v != []:
                return normalize(v, "employmentAgencyLicenseNumber")
          

class SSIC(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    primaryCode : Optional[dict] = Field(..., alias='trainingProvider')
    secondaryCode : Optional[dict] = Field(..., alias='trainingProvider')
 

    @validator("primaryCode")
    def validate_primaryCode(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ssic", "primaryCode")

    @validator("secondaryCode")
    def validate_secondaryCode(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "ssic", "secondaryCode")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class Address(BaseModel):
    id : Optional[dict] = Field(..., alias='trainingProvider')
    uen : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    unit : Optional[dict] = Field(..., alias='trainingProvider')
    block : Optional[dict] = Field(..., alias='trainingProvider')
    floor : Optional[dict] = Field(..., alias='trainingProvider')
    street : Optional[dict] = Field(..., alias='trainingProvider')
    typeId : Optional[dict] = Field(..., alias='trainingProvider')
    building : Optional[dict] = Field(..., alias='trainingProvider')
    postalCode : Optional[dict] = Field(..., alias='trainingProvider')
  
    @validator("id")
    def validate_id(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "id")[0]

    @validator("uen")
    def validate_uen(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "uen")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

    @validator("unit")
    def validate_unit(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "unit")[0]
    
    @validator("block")
    def validate_block(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "block")[0]
    
    @validator("floor")
    def validate_floor(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "floor")[0]

    @validator("street")
    def validate_street(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "street")[0]
    
    @validator("typeId")
    def validate_typeId(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "typeId")[0]

    @validator("building")
    def validate_building(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "building")[0]

    @validator("postalCode")
    def validate_postalCode(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "address", "postalCode")[0]


class TrainingProviderOutcome(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    outcomeAreas : Optional[dict] = Field(..., alias='trainingProvider')
    overallOutcome : Optional[dict] = Field(..., alias='trainingProvider')
    numberOfRespondents : Optional[dict] = Field(..., alias='trainingProvider')
  

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"outcome",  "meta"), "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "updateDate")

    @validator("outcomeAreas")
    def validate_outcomeAreas(cls, v):
        if v is not None and v != []:
                return normalize_list3(normalize_dict(v,"outcome", "outcomeAreas"), "areaOfTraining")[0]
    
    @validator("overallOutcome")
    def validate_overallOutcome(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"outcome", "overallOutcome"), "average")

    @validator("numberOfRespondents")   
    def validate_numberOfRespondents(cls, v):
        if v is not None and v != []:
                return normalize_dict(v,"outcome", "numberOfRespondents")

class OutcomeAreas(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    areaOfTraining : Optional[dict] = Field(..., alias='trainingProvider')
    average : Optional[dict] = Field(..., alias='trainingProvider')
    starsRating : Optional[dict] = Field(..., alias='trainingProvider')
    numberOfRespondents : Optional[dict] = Field(..., alias='trainingProvider')


    @validator("average")
    def validate_average(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "outcomeAreas")[0], "average")

    @validator("starsRating")
    def validate_starsRating(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "outcomeAreas")[0], "starsRating")

    @validator("numberOfRespondents")
    def validate_numberOfRespondents(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "outcomeAreas")[0], "starsRating")

    @validator("areaOfTraining")
    def validate_areaOfTraining(cls, v):
        if v is not None and v != []:
                return normalize_list3(normalize_dict(v, "outcome", "outcomeAreas"), "areaOfTraining")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"outcome",  "meta"), "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "updateDate")

class TrainingProviderOverallOutcome(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    average : Optional[dict] = Field(..., alias='trainingProvider')
    starsRating : Optional[dict] = Field(..., alias='trainingProvider')
    numberOfRespondents : Optional[dict] = Field(..., alias='trainingProvider')


    @validator("average")
    def validate_average(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "overallOutcome"), "average")

    @validator("starsRating")
    def validate_starsRating(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "overallOutcome"), "starsRating")

    @validator("numberOfRespondents")
    def validate_numberOfRespondents(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "overallOutcome"), "starsRating")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"outcome",  "meta"), "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "outcome", "meta"), "updateDate")

class TrainingProviderQuality(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    qualityAreas : Optional[dict] = Field(..., alias='trainingProvider')
    overallQuality : Optional[dict] = Field(..., alias='trainingProvider')
    numberOfRespondents : Optional[dict] = Field(..., alias='trainingProvider')
   
    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

    @validator("qualityAreas")
    def validate_qualityAreas(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"quality", "qualityAreas")[0], "starsRating")
    
    @validator("overallQuality")
    def validate_overallQuality(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"quality", "overallQuality"), "average")

    @validator("numberOfRespondents")
    def validate_numberOfRespondents(cls, v):
        if v is not None and v != []:
                return normalize_dict(v,"quality",  "numberOfRespondents")

class TrainingProviderOverallQuality(BaseModel):
    average : Optional[dict] = Field(..., alias='trainingProvider')
    starsRating : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')


    @validator("average")
    def validate_average(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "quality", "overallQuality"), "average")

    @validator("starsRating")
    def validate_starsRating(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "quality", "overallQuality"), "starsRating")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "meta", "updateDate")

class QualityAreas(BaseModel):
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    starsRating : Optional[dict] = Field(..., alias='trainingProvider')
    averageRating : Optional[dict] = Field(..., alias='trainingProvider')
    areaOfTraining : Optional[dict] = Field(..., alias='trainingProvider')
    numberOfRespondents : Optional[dict] = Field(..., alias='trainingProvider')

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize_dict(normalize_dict(v, "quality", "qualityAreas")[0], "meta", "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize_dict(normalize_dict(v, "quality", "qualityAreas")[0], "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize_dict(normalize_dict(v,"quality",  "qualityAreas")[0], "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize_dict(normalize_dict(v, "quality", "qualityAreas")[0], "meta", "updateDate")

    @validator("starsRating")
    def validate_starsRating(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize(normalize_dict(v,"quality", "qualityAreas")[0], "starsRating")

    @validator("averageRating")
    def validate_averageRating(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize(normalize_dict(v,"quality", "qualityAreas")[0], "averageRating")

    @validator("areaOfTraining")
    def validate_areaOfTraining(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize(normalize_dict(v,"quality", "qualityAreas")[0], "areaOfTraining")

    @validator("numberOfRespondents")
    def validate_numberOfRespondents(cls, v):
        if v.get("quality") is not None and v != []:
            return normalize(normalize_dict(v,"quality", "qualityAreas")[0], "numberOfRespondents")

class Notification(BaseModel):
    jobPostExpired : Optional[dict] = Field(..., alias='trainingProvider')
    applicationReceived : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    
        
    @validator("jobPostExpired")
    def validate_jobPostExpired(cls, v):
        if v.get("notification") is not None and v != []:
            return normalize_dict(v, "notification", "jobPostExpired")

    @validator("applicationReceived")
    def validate_applicationReceived(cls, v):
        if v.get("notification") is not None and v != []:
            return normalize_dict(v, "notification", "applicationReceived")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v.get("notification") is not None and v != []:
            return normalize_dict(v, "meta", "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v.get("notification") is not None and v != []:
            return normalize_dict(v, "meta", "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v.get("notification") is not None and v != []:
            return normalize_dict(v, "meta", "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v.get("notification") is not None and v != []:
            return normalize_dict(v, "meta", "updateDate")

    
class ContactNumber(BaseModel):
    id : Optional[dict] = Field(..., alias='trainingProvider')
    uen : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')
    typeId : Optional[dict] = Field(..., alias='trainingProvider')
    number : Optional[dict] = Field(..., alias='trainingProvider')
    areaCode : Optional[dict] = Field(..., alias='trainingProvider')
    countryCode : Optional[dict] = Field(..., alias='trainingProvider')
    internationalPrefix : Optional[dict] = Field(..., alias='trainingProvider')
    
    @validator('id')
    def check_id(cls, v):
        if v.get("notification") is not None and v != []:
                return normalize_dict(v, "contactNumber", 'id')[0]
    
    @validator('uen')
    def check_uen(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "contactNumber", 'uen')[0]
    
    @validator('createdBy')
    def check_createdBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, 'meta', 'createBy')
    
    @validator('updatedBy')
    def check_updatedBy(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, 'meta', 'updateBy')

    @validator('createdDate')
    def check_createdDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, 'meta', 'createDate')

    @validator('updatedDate')
    def check_updatedDate(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, 'meta', 'updateDate')

    @validator('typeId')
    def check_typeId(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "contactNumber", 'typeId')[0]

    @validator('number')
    def check_number(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"contactNumber",  'telephone')[0], "number")

    @validator('areaCode')
    def check_areaCode(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "contactNumber", 'telephone')[0], "areaCode")

    @validator('countryCode')
    def check_countryCode(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "contactNumber", 'telephone')[0], "countryCode")

    @validator('internationalPrefix')
    def check_internationalPrefix(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "contactNumber", 'telephone')[0], "internationalPrefix")




class TrainingProviderTelePhone(BaseModel):
    number : Optional[dict] = Field(..., alias='trainingProvider')
    areaCode : Optional[dict] = Field(..., alias='trainingProvider')
    countryCode : Optional[dict] = Field(..., alias='trainingProvider')
    internationalPrefix : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator('number')
    def check_number(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v,"contactNumber",  'telephone')[0], "number")

    @validator('areaCode')
    def check_areaCode(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "contactNumber", 'telephone')[0], "areaCode")

    @validator('countryCode')
    def check_countryCode(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "contactNumber", 'telephone')[0], "countryCode")

    @validator('internationalPrefix')
    def check_internationalPrefix(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "contactNumber", 'telephone')[0], "internationalPrefix")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class ForeignAddress(BaseModel):
    id : Optional[dict] = Field(..., alias='trainingProvider')
    uen : Optional[dict] = Field(..., alias='trainingProvider')
    typeId : Optional[dict] = Field(..., alias='trainingProvider')
    address1 : Optional[dict] = Field(..., alias='trainingProvider')
    address2 : Optional[dict] = Field(..., alias='trainingProvider')
    countryCode : Optional[dict] = Field(..., alias='trainingProvider')
    createdBy : Optional[dict] = Field(..., alias='trainingProvider')
    updatedBy : Optional[dict] = Field(..., alias='trainingProvider')
    createdDate : Optional[dict] = Field(..., alias='trainingProvider')
    updatedDate : Optional[dict] = Field(..., alias='trainingProvider')


    @validator("id")
    def validate_id(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress", "id")
        
    @validator("uen")
    def validate_uen(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress","uen")

    @validator("typeId")
    def validate_typeId(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress","typeId")

    @validator("address1")
    def validate_address1(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress", "address1")

    @validator("address2")
    def validate_address2(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress", "address2")
    
    @validator("countryCode")
    def validate_countryCode(cls, v):
        if v is not None and v != []:
                return normalize_dict(v, "foreignAddress", "countryCode")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "foreignAddress", "meta"), "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "foreignAddress", "meta"), "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "foreignAddress", "meta"), "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(normalize_dict(v, "foreignAddress", "meta"), "updateDate")
    
class StatisticsSummary(BaseModel):    
    pageViewCount : Optional[dict] = Field(..., alias='statisticsSummary')
    courseClaimCount : Optional[dict] = Field(..., alias='statisticsSummary')
    courseReferenceNumber : Optional[dict] = Field(..., alias='statisticsSummary')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("pageViewCount")
    def validate_pageViewCount(cls, v):
        if v is not None and v != []:
                return normalize(v, "pageViewCount")
        
    @validator("courseClaimCount")
    def validate_courseClaimCount(cls, v):
        if v is not None and v != []:
                return normalize(v, "courseClaimCount")

    @validator("courseReferenceNumber")
    def validate_courseReferenceNumber(cls, v):
        if v is not None and v != []:
                return normalize(v, "courseReferenceNumber")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class MethodOfDeliveries(BaseModel):
    code : Optional[list] = Field(..., alias='methodOfDeliveries')
    description : Optional[list] = Field(..., alias='methodOfDeliveries')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class LocationOfTrainings(BaseModel):
    code : Optional[list] = Field(..., alias='locationOfTrainings')
    description : Optional[list] = Field(..., alias='locationOfTrainings')    
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class MediumOfInstructions(BaseModel):
    code : Optional[list] = Field(..., alias='mediumOfInstructions')
    description : Optional[list] = Field(..., alias='mediumOfInstructions')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
   

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class TargetTrainingGroups(BaseModel):
    code : Optional[list] = Field(..., alias='targetTrainingGroups')
    description : Optional[list] = Field(..., alias='targetTrainingGroups')    
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
  

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "code")[0]
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize_list3(v, "description")[0]

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class QualificationAttained(BaseModel):
    code : Optional[dict] = Field(..., alias='qualificationAttained')
    description : Optional[dict] = Field(..., alias='qualificationAttained')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')
   

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class PublicFundingIndicator(BaseModel):
    code : Optional[dict] = Field(..., alias='publicFundingIndicator')
    description : Optional[dict] = Field(..., alias='publicFundingIndicator')    
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class TargetWorkForceSegment(BaseModel):
    code : Optional[dict] = Field(..., alias='targetWorkforceSegment')
    description : Optional[dict] = Field(..., alias='targetWorkforceSegment')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')


    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class MinimumEducationRequirements(BaseModel):
    code : Optional[dict] = Field(..., alias='minimumEducationRequirements')
    description : Optional[dict] = Field(..., alias='minimumEducationRequirements')
    createdBy : Optional[dict] = Field(..., alias='meta')
    updatedBy : Optional[dict] = Field(..., alias='meta')
    createdDate : Optional[dict] = Field(..., alias='meta')
    updatedDate : Optional[dict] = Field(..., alias='meta')

    @validator("code")
    def validate_code(cls, v):
        if v is not None and v != []:
                return normalize(v, "code")
        
    @validator("description")
    def validate_description(cls, v):
        if v is not None and v != []:
                return normalize(v, "description")

    @validator("createdBy")
    def validate_createBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "createBy")
        
    @validator("updatedBy")
    def validate_updateBy(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateBy")

    @validator("createdDate")
    def validate_createDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "createDate")

    @validator("updatedDate")
    def validate_updateDate(cls, v):
        if v is not None and v != []:
                return normalize(v, "updateDate")

class SearchCoursePayload(BaseModel):
    dateTo: Optional[str]
    dateFrom: Optional[str]
    tags: Optional[str]
    supportingCodes: Optional[str]
    sortField : Optional[str]
    sortOrder : Optional[str]

class CourseDetailsResponse(BaseModel):
    createBy: Optional[str]
    updateBy: Optional[str]
    createDate: Optional[str]
    updateDate: Optional[str]
    course: str 