<template>
   <div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('SeeAdvising')">See All Advising forms</button>
  </div>
  <div v-show ="showMnumber">
     <form v-on:submit.prevent="getadvsing" class="getadvsing">
      <label for="CostAd">Enter Mnumber</label><br />
    <input type="text" id="CostAd" name="CostAd" v-model ="PStudentID">
    <div class="submit">
      <button>Submit</button>
    </div>
     </form> 
  </div>
<div>
<form v-on:submit.prevent="UpdateAdvising" class="Updateadvsing" v-show="showform">
    <div ref="content">
      <h1>Enter Advising Form</h1>
      <label for="Fname">FirstName:</label><br />
      <input type="text" id="Fname" name="Fname" v-model="tosend.FirstName" :placeholder="PFirstName"/>

      <label for="Lname">LastName:</label><br />
      <input
        type="text"
        id="Lname"
        name="Lname"
        v-model="tosend.LastName"
        :placeholder="PLastName"
      /><br />

      <label for="Mnumber">Mnumber:</label><br />
      <input
        type="text"
        id="StudentID"
        name="StudentID"
        
        v-model="tosend.StudentID"
        :placeholder="PStudentID"
      /><br />
      <label for="Semester">Choose a Semester:</label>
      <select name="Semester" id="Semester"  v-model="PSemester" >
        <option value="Fall">Fall</option>
        <option value="Spring">Spring</option>
        <option value="Summer1">Summer1</option>
        <option value="Summer2">Summer2</option>
      </select>

      <label for="year">Choose a Year:</label>
      <select name="year" id="year"  v-model="PYear">
        <option value="2021">2021</option>
        <option value="2022">2022</option>
      </select>

      <label for="Classification">Choose a Classification:</label>
      <select
        name="Classification"
        id="Classification"
        
        v-model="PClassification"

      >
        <option value="Freshman">Freshman</option>
        <option value="Sophomore">Sophomore</option>
        <option value="junior">junior</option>
        <option value="Senior">Senior</option>
      </select>

      <label for="Major">Major:</label><br />
      <input type="text"  list="Major"  v-model="PMajor" />
      <datalist name="Major" id="Major">
        <option v-for="item in Majors" :key="item" :value="item" />
      </datalist>
      <label for="ListofCourses">ListofCourses:</label><br />
      <input
        type="text"
        id="ListofCourses"
        name="ListofCourses"
        
        v-model="tosend.ListofCourses"
        :placeholder="PListofCourses"
      /><br />

      <label for="DateCreated">DateCreated:</label>
      <input
        type="date"
        id="DateCreated"
        name="DateCreated"
        
        v-model="PDateCreated"
        
      />
    </div>
    <div v-if="passwordError" class="error">{{ passwordError }}</div>
    <div id="addstuff" ref="addstuff"></div>
    <div class="submit">
      <button>Submit form</button>
    </div>
  </form>
  </div>
  
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tosend: {
        Semester: "",
        Year: 0,
        StudentID: "",
        ListofCourses: "",
        DateCreated: "",
        Classification: "",
        Major: "",
        FirstName: "",
        LastName: "",
      },
      post: false,
      passwordError: "",
      htmldoc: "",
      image: "",
      Majors: [
        "Accounting, B.B.A.",
        "Applied Arts and Sciences, B.A.A.S.",
        "Art B.F.A. with Teacher Certification",
        "Art, B.A.",
        "Art, B.F.A.",
        "Athletic Training, B.S.A.T.",
        "Bilingual Generalist and General Education EC-6, B.S.I.S. (Spanish)",
        "Biology, B.S.",
        "Biology-Life Science, B.S. with Secondary Certification (Grades 7-12)",
        "Chemistry, B.S.",
        "Composite Science, B.S. with Secondary Certification (Grades 7-12)",
        "Computer Science, B.A.",
        "Computer Science, B.S.",
        "Criminal Justice, B.S.C.J.",
        "Dental Early Admissions Program ",
        "Dental Hygiene, B.S.D.H.",
        "Early Childhood Through Grade 6 (EC-6), B.S.I.S.",
        "Economics, B.B.A.",
        "English, B.A.",
        "Exercise Physiology, B.S.E.P.",
        "Finance, B.B.A.",
        "French ",
        "General Business, B.B.A.",
        "Geosciences, B.S.",
        "Global Studies, B.A.",
        "Humanities, B.A.",
        "Kinesiology  B.A. ",
        "Kinesiology  B.S.",
        "Management Information Systems, B.B.A.",
        "Management, B.B.A.",
        "Marketing, B.B.A.",
        "Mass Communication, B.A.",
        "Mathematics (4-8 Certificate), B.S.I.S.",
        "Mathematics, B.A.",
        "Mathematics, B.S.",
        "Mathematics, B.S. with Secondary Certification (Grades 7-12)",
        "Mechanical Engineering, B.S.M.E.",
        "Music Instrumental Emphasis, B.M. ",
        "Music Vocal Emphasis, B.M. ",
        "Music, B.A.",
        "Music, B.M.",
        "Nursing - Accelerated Second Bachelor’s B.S.N. (Pre-licensure)",
        "Nursing - RN Transition Program, B.S.N. (Post-licensure)",
        "Nursing, B.S.N. (Pre-licensure)",
        "Physics, B.S.",
        "Political Science, B.A.",
        "Psychology, B.A.",
        "Psychology, B.S.",
        "Radiologic Sciences, B.S.R.S.",
        "Radiologic Technology, B.S.R.T.",
        "Registered Respiratory Therapist-to-BSRC Program",
        "Respiratory Care, B.S.R.C.",
        "Social Studies (4-8 Certificate), B.S.I.S.",
        "Social Work, B.S.W.",
        "Sociology, B.A.",
        "Sociology, B.S.",
        "Spanish (Grades EC-12, All-Level), B.A. with Teacher Certification",
        "Spanish, B.A.",
        "Special Education Early Childhood B.S.I.S.",
        "Sport and Leisure Studies, B.A.",
        "Sport and Leisure Studies, B.S.",
        "Theatre B.F.A. Teacher Certification",
        "Theatre, B.F.A.",
      ],
      PSemester: "",
      PYear: "",
      PStudentID: "",
      PListofCourses: "No List Of Courses",
      PDateCreated: "",
      PClassification: "",
      PMajor: "",
      PFirstName: "No First Name",
      PLastName: "No Last Name",
      showform: false,
      showMnumber: true,
      answer: {},
      post: "",
    };
  },
  methods: {
    getadvsing() {
      axios
        .get("http://143.244.153.25:8004/Advising/student/" + this.PStudentID)
        .then((res) => {
          this.answer = res.data[0];
          console.log(res.data)
          console.log(this.answer);
          if (res.data != "Invalid number") {
            if (this.answer.FirstName != "") {
              this.PFirstName = this.answer.FirstName;
            }
            if (this.answer.LastName != "") {
              this.PLastName = this.answer.LastName;
            }
            if (this.answer.StudentID != "") {
              this.PStudentID = this.answer.StudentID;
              this.tosend.StudentID = this.PStudentID;
            }
            if (this.answer.Semester != "") {
              this.PSemester = this.answer.Semester;
            }
            if (this.answer.Year != "") {
              this.PYear = this.answer.Year;
            }
            if (this.answer.Major != "") {
              this.PMajor = this.answer.Major;
            }
            if (this.answer.Classification != "") {
              this.PClassification = this.answer.Classification;
            }
            if (this.answer.DateCreated != "") {
              this.PDateCreated = this.answer.DateCreated;
            }
            if (this.answer.ListofCourses != "") {
              this.PListofCourses = this.answer.ListofCourses;
            }
            this.showMnumber = false;
            this.showform = true;
            this.tosend.Classification = this.PClassification;
            this.tosend.Semester = this.PSemester;
            this.tosend.Year = this.PYear;
            this.tosend.Major = this.PMajor;
             this.tosend.DateCreated = this.PDateCreated;
          } else {
            this.passwordError = "Invalid Mnumber";
          }
        })
        .catch((error) => {
          // error.response.status Check status code
          this.passwordError = error.statuscode;
        })
        .finally(() => {
          //Perform action in always
          console.log("final");
        });
    },
    reset() {
      this.post = false;
      for (let field in this.tosend) {
        this.tosend[field] = "";
      }
    },
    UpdateAdvising() {
      var otherdic = {};
      for (var things in this.tosend) {
        if (this.tosend[things] != "") {
          otherdic[things] = this.tosend[things];
        }
      }

      axios
        .patch(
          "http://143.244.153.25:8004/UpdateAdvisingForm",
          JSON.stringify(otherdic),
          { headers: { "Content-Type": "application/json" } }
        )
        .then((res) => {
          //Perform Success Action
          // JSON responses are automatically parsed.
          this.post = res.data;

          if (this.post["success"] == true) {
            this.reset();
            this.passwordError = "Updated!!";
          } else {
            this.passwordError = this.post["error"];
          }
        })
        .catch((error) => {
          // error.response.status Check status code
          this.passwordError = error.statuscode;
        })
        .finally(() => {
          //Perform action in always
        });
    },
  },
};
</script>

<style scoped>
form {
  max-width: 650px;
  margin: 30px auto;
  background: white;
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}
label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.6em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}
input,
select {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}
button {
  background: #0b6dff;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
}
.submit {
  text-align: center;
}
.error {
  color: #ff0062;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
</style>