
# Midterm Paired Task 1.
### ***Object Oriented Analysis and Design***

1.	**Following the OO workflow as discussed in class**, you are task to design the OO Model of the given problem (use draw.io) of the scenario below:

**Problem Statement. Tiny Hospital** keeps information on **patients** and **hospital rooms**. The system assigns each patient a patient ID number. In addition, the patient’s name and date of birth are recorded. Some patients are resident patients (they spend at least one night in the hospital) and others are outpatients (they are treated and released). Resident patients are assigned to a room. Each room is identified by a room number. The **Tiny hospital system** also stores the room type (private or semi-private) and room fee. Overtime, each room will have many patients who stay in it. Each resident patient will stay in only one room. The hospital system has features that can view patient information and view whether a room is occupied or not. Both patient and room entities must have features that allows adding, updating and searching of records.

## **STEP1. IDENTIFY** all the necessary **OBJECT** within the problem domain.

### •	Patient
### •	Resident Patient
### • OutPatient
### •	Hospital Room
### •	Hospital Flow

## **STEP 2. IDENTIFY all the properties and methods/behaviors in the problem statement.**

### ***Patient***
  #### > patientID &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - addPatient()
  #### > name &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  --->  Behavior &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  -updatePatient()
  #### > dateOfBirth  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -searchPatientinfo()
  #### > patientType &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -getPatientinfo()
---

 ### ***ResPatient***
#### > roompatient &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ---> Behavior &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -assignRoom()


#### > OutPatient &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ---> Behavior &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -discharge()
---

### ***HosRoom***
#### > roomNumber
#### > roomType &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -assignPatient()
#### > roomFee &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ---> Behavior &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -releasePatient()
#### > occupied &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -isOccupied()
---

### ***HosFlow***

#### > patientList &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ---> Behavior &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -addPatient()
#### > roomList &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -updatePatient()
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -searchPatient()

 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -viewPatient()

 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -viewRstat()
 
---
## **STEP 3. Design the MODEL using a Class Diagram** (You may use draw.io to represent the Blueprint of all the class that you need to create)
<img alt="image" src="https://github.com/tayting05/7OOP-Lab-Task/blob/dba8cb693959f21c24331e1a863b72a50a449e64/images/Class%20Diagram%201.png" />

---
## **STEP 4. Implement the class using Java code** construct of each interacting entities that you have identified.

<img  src="https://github.com/tayting05/7OOP-Lab-Task/blob/dba8cb693959f21c24331e1a863b72a50a449e64/images/Patient%20Method.png" >
<img  src="https://github.com/tayting05/7OOP-Lab-Task/blob/dba8cb693959f21c24331e1a863b72a50a449e64/images/Patient%20Method%202.png" >
<img  src="https://github.com/tayting05/7OOP-Lab-Task/blob/3bd08cd79cc9b15ee1db196fdd35be6360fa7a2f/images/Patient%20Method%203.png" >
<img  src="https://github.com/tayting05/7OOP-Lab-Task/blob/3bd08cd79cc9b15ee1db196fdd35be6360fa7a2f/images/HosRoom%20Method.png" >
<img  src="https://github.com/tayting05/7OOP-Lab-Task/blob/3bd08cd79cc9b15ee1db196fdd35be6360fa7a2f/images/Hospital%20Flow%20Method.png" >
<img  src="https://github.com/tayting05/7OOP-Lab-Task/blob/3bd08cd79cc9b15ee1db196fdd35be6360fa7a2f/images/Main%20Method.png" >

---
## **Note: Highlight all the outputs following the example from STEP 1 to STEP 4 as shown in the lecture**

