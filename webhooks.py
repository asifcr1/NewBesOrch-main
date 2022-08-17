from time import sleep
from data.schema import *
import requests
import json as js

webhooks = {
        "course" : "https://catch.tadabase.io/webhook/LmavlZtBd3",
        "course_run" : "https://catch.tadabase.io/webhook/PnazvxUPaO",
        "insert_submission_type" : "https://catch.tadabase.io/webhook/0.1wboVQCoax",
        "insert_courseVacancy" : "https://catch.tadabase.io/webhook/9pdBNOtZd8",
        "insert_scheduleInfoType" : "https://catch.tadabase.io/webhook/y7aANAsmbg",
        "insert_fees" : "https://catch.tadabase.io/webhook/LqdP73sDbl",
        "insert_tags" : "https://catch.tadabase.io/webhook/rRbD1Wf6d6",
        "insert_status" : "https://catch.tadabase.io/webhook/1qdGvXsybN",
        "insert_cluster" : "https://catch.tadabase.io/webhook/mBdJy1h4b0",
        "insert_outcome" : "https://catch.tadabase.io/webhook/9jaK1BtAdk",
        "insert_quality" : "https://catch.tadabase.io/webhook/BXdL7lhobJ",
        "insert_sectors" : "https://catch.tadabase.io/webhook/JvaMw2Codp",
        "insert_support" : "https://catch.tadabase.io/webhook/KBe1WxijbX",
        "insert_brochure" : "https://catch.tadabase.io/webhook/QzaOMzhPdp",
        "insert_category" : "https://catch.tadabase.io/webhook/LqdP7EuDbl",
        "insert_taggings" : "https://catch.tadabase.io/webhook/9pdBNGiZd8",
        "insert_jobLevels" : "https://catch.tadabase.io/webhook/rRbD1Ou6d6",
        "insert_wsqFrameworks" : "https://catch.tadabase.io/webhook/1qdGvOhybN",
        "insert_areaOfTrainings" : "https://catch.tadabase.io/webhook/mBdJywc4b0",
        "insert_eduOfTargetAuds" : "https://catch.tadabase.io/webhook/9jaK1qIAdk",
        "insert_fieldOfStudies1" : "https://catch.tadabase.io/webhook/BXdL7EcobJ",
        "insert_fieldOfStudies2" : "https://catch.tadabase.io/webhook/JvaMwrtodp",
        "insert_modeOfTrainings" : "https://catch.tadabase.io/webhook/01dNLqfnaX",
        "insert_skillsFrameworks" : "https://catch.tadabase.io/webhook/QzaOM4cPdp",
        "insert_subSectors" : "https://catch.tadabase.io/webhook/y7aA6Ycmbg",
        "insert_tracks" : "https://catch.tadabase.io/webhook/nPeEqECAep",
        "insert_occupations" : "https://catch.tadabase.io/webhook/1qdGROhybN",
        "insert_jobRoles" : "https://catch.tadabase.io/webhook/mBdJ8wS4a0",
        "insert_mappedSkillsCompetency" : "https://catch.tadabase.io/webhook/9jaK8qTAbk",
        "insert_generic" : "https://catch.tadabase.io/webhook/gQbWP0.1tpd6",
        "insert_keyTask" : "https://catch.tadabase.io/webhook/BleXQ1i6ar",
        "insert_technical" : "https://catch.tadabase.io/webhook/O8bY74U0e7",
        "insert_minimumEducationRequirements" : "https://catch.tadabase.io/webhook/jZdywxsjaJ",
        "insert_targetWorkForceSegment" : "https://catch.tadabase.io/webhook/EMax6mSGd0.1",
        "insert_publicFundingIndicator" : "https://catch.tadabase.io/webhook/XKdw0AcOeg",
        "insert_qualificationAttained" : "https://catch.tadabase.io/webhook/YjbqQot4bL",
        "insert_targetTrainingGroups" : "https://catch.tadabase.io/webhook/xgepZoclb1",
        "insert_mediumOfInstructions" : "https://catch.tadabase.io/webhook/0.1wboZJUoax",
        "insert_locationOfTrainings" : "https://catch.tadabase.io/webhook/0yelRDT9bE",
        "insert_methodOfDeliveries" : "https://catch.tadabase.io/webhook/xmbmq8C0bo",
        "insert_statisticsSummary" : "https://catch.tadabase.io/webhook/pgenR6cyeN",
        "insert_trainingProvider" : "https://catch.tadabase.io/webhook/Pnaz6zUPaO",
        "insert_ssic" : "https://catch.tadabase.io/webhook/9pdBrGiZd8",
        "insert_address" : "https://catch.tadabase.io/webhook/rRbDqOu6d6",
        "insert_outcomeAreas" : "https://catch.tadabase.io/webhook/BXdLZEfoaJ",
        "insert_overallOutcome" : "https://catch.tadabase.io/webhook/JvaMZrhobp",
        "insert_qualityAreas" : "https://catch.tadabase.io/webhook/01dNOqhneX",
        "insert_overallQuality" : "https://catch.tadabase.io/webhook/QzaOg4uPap",
        "insert_notification" : "https://catch.tadabase.io/webhook/LqdPj3fDal",
        "insert_contactNumber" : "https://catch.tadabase.io/webhook/P9aQkDcDdD",
        "insert_telephone" : "https://catch.tadabase.io/webhook/RMdRlQUKal",
        "insert_foreignAddress" : "https://catch.tadabase.io/webhook/pZeVvwF4eG",
        "insert_contactPersonEmail" : "https://catch.tadabase.io/webhook/KBe16xtjaX",
        "insert_trainerCourseContent" : "https://catch.tadabase.io/webhook/RBe3y1H8bL",
        "insert_customerService" : "https://catch.tadabase.io/webhook/YWb4z8FjeZ",
        "insert_betterJobPerformance" : "https://catch.tadabase.io/webhook/wKe0.1R9Cna3",
        "insert_ableToApplyLearning" : "https://catch.tadabase.io/webhook/Arb6BXs3by",
        "insert_expandedJobScope" : "https://catch.tadabase.io/webhook/DGe7p9iPan",
        "insert_period" : "https://catch.tadabase.io/webhook/pzb8MMSJdE",
        "insert_contactPerson" : "https://catch.tadabase.io/webhook/YWb468ujeZ",
        "insert_learning" : "https://catch.tadabase.io/webhook/j6e9DgSZdW"
    }   

headers = {
            'Content-Type': 'application/json',
          }


def InsertMinimumEducationRequirements(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_minimumEducationRequirements"), headers=headers, data=js.dumps(data))
    return response.json() 

def InsertTargetWorkForceSegment(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_targetWorkForceSegment"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTrainingProviderOverallQuality(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_overallQuality"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertQualityAreas(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_qualityAreas"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTrainingProviderQuality(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_quality"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertPublicFundingIndicator(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_publicFundingIndicator"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertQualificationAttained(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_qualificationAttained"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTargetTrainingGroups(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_targetTrainingGroups"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertMediumOfInstructions(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_mediumOfInstructions"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertLocationOfTrainings(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_locationOfTrainings"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertMethodOfDeliveries(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_methodOfDeliveries"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertStatisticsSummary(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_statisticsSummary"), headers=headers, data=js.dumps(data))
    return response.json()


def InsertForeignAddress(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_foreignAddress"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTelephone(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_telephone"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertContactNumber(data):
    sleep(0.1)
    data = { "data" : data }    
    response = requests.post(webhooks.get("insert_contactNumber"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertNotification(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_notification"), headers=headers, data=js.dumps(data))
    return response.json()


def InsertOverallOutcome(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_overallOutcome"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertOutcomeAreas(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_outcomeAreas"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertOutcome(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_outcome"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertAddress(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_address"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertSSIC(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_ssic"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTrainingProvider(data):
    sleep(0.1)
    data = { "data" : data}
    response = requests.post(webhooks.get("insert_trainingProvider"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTechnical(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_technical"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertKeyTask(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_keyTask"), headers=headers, data=js.dumps(data))
    return response.json()
    
def InsertGeneric(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_generic"), headers=headers, data=js.dumps(data))
    return response.json()
    
def InsertMappedSkillsCompetency(data):  
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_mappedSkillsCompetency"), headers=headers, data=js.dumps(data))
    return response.json()


def InsertOccupations(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_occupations"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTracks(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_tracks"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertSubSectors(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_subSectors"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertSkillsFrameworks(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_skillsFrameworks"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertModeOfTrainings(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_modeOfTrainings"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertFieldOfStudies1(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_fieldOfStudies1"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertFieldOfStudies2(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_fieldOfStudies2"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertEduOfTargetAuds(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_eduOfTargetAuds"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertAreaOfTrainings(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_areaOfTrainings"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertWsqFrameworks(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_wsqFrameworks"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertEmailAddress(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_contactPersonEmail"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertContactPerson(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_contactPerson"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertJobLevels(data): 
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_jobLevels"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTaggings(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_taggings"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertJobRoles(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_jobRoles"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertCategory(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_category"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertBrochure(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_brochure"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertPeriod(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_period"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertSupport(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_support"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertSectors(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_sectors"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertTrainerCourseContent(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_trainerCourseContent"), headers=headers, data=js.dumps(data))
    return response.json()
def InsertCustomerService(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_customerService"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertOverallQuality(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_overallQuality"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertLearning(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_learning"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertQuality(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_quality"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertBetterJobPerformance(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_betterJobPerformance"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertAbleToApplyLearning(data):    
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_ableToApplyLearning"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertExpandedJobScope(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_expandedJobScope"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertCluster(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_cluster"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertStatus(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_status"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertView(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_view"), headers=headers, data=js.dumps(data))
    return response.json()
    
def InsertTags(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_tags"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertScheduleInfoType(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_scheduleInfoType"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertCourseVacancy(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_courseVacancy"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertRuns(data):
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("course_run"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertFees(data):    
    sleep(0.1)
    data = { "data" : data }
    response = requests.post(webhooks.get("insert_fees"), headers=headers, data=js.dumps(data))
    return response.json()

def InsertCourse(data):
    sleep(0.1)
    data = { "data" : data }
    print(type(data))
    response = requests.post(webhooks.get("course"), headers=headers, json=data)
    return response.json()    