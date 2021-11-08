<template>
  <h1>Midwestern State University Advising Form</h1>
  
  <div>
      <button @click="$router.push('mainpage')">Home</button>
      <button @click="$router.push('EditAdvising')">Edit Advising forms</button>
    </div>
    <br><br>
     <form v-on:submit.prevent="Seeform" class="SeeAdvisng">
 <div>
    Semester<select name="Semester" id="Semester" v-model="tosend.Semester">
      <option value="Fall">Fall</option>
      <option value="Spring">Spring</option>
      <option value="Summer1">Summer1</option>
      <option value="Summer2">Summer2</option></select
    >&ensp;&ensp;&ensp; Year<select name="year" id="year" v-model="tosend.Year">
      <option value="2022">2022</option>
      <option value="2021">2021</option></select
    >
    &ensp;&ensp;&ensp;&ensp;&ensp; FirstName<input
      type="text"
      id="Fname"
      name="Fname"
      v-model="tosend.FirstName"
    />&ensp;&ensp;&ensp;&ensp;&ensp; LastName<input
      type="text"
      id="Lname"
      name="Lname"
      v-model="tosend.LastName"
    /><br /><br />

    Mnumber<input
      type="text"
      id="StudentID"
      name="StudentID"
      v-model="tosend.StudentID"
    />&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 
    Major<input type="text"  list="Major"  v-model="tosend.Major" />
      <datalist name="Major" id="Major">
        <option v-for="item in Majors" :key="item" :value="item" />
      </datalist>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Classification
    <select
      name="Classification"
      id="Classification"
      v-model="tosend.Classification"
    >
      <option value=""></option>
      <option value="Freshman">Freshman</option>
      <option value="Sophomore">Sophomore</option>
      <option value="junior">junior</option>
      <option value="Senior">Senior</option></select
    >&ensp;&ensp;&ensp;&ensp;&ensp; Display
    <select name="Display" id="Display" v-model="tosend.Display">
      <option value="25">25</option>
      <option value="50">50</option>
      <option value="100">100</option></select
    >&ensp;&ensp;&ensp;&ensp;&ensp;
  </div>
  <br />
  <div class="submit">
    <button>GO</button>
  </div>
    </form>
 <div ref="tableadd" id ="tableadd" >
   <table v-show="hasArrived">
    <tr>
    <th>Semester</th>
    <th>Year</th>
    <th>StudentID</th>
    <th>ListofCourses</th>
    <th>Date Created </th>
    <th>FirstName</th>
    <th>LastName</th>
    <th>Classification</th>
    <th>Major</th>
  </tr>
    <tr v-for="item in tableStuff" v-show ="hasTable"> 
      <th>{{item.Semester}}</th>
      <th>{{item.Year}}</th>
      <th>{{item.StudentID}}</th>
      <th>{{item.ListofCourses}}</th>
      <th>{{item.DateCreated}}</th>
      <th>{{item.FirstName}}</th>
      <th>{{item.LastName}}</th>
      <th>{{item.Classification}}</th>
      <th>{{item.Major}}</th>
    </tr>
   </table>
  </div>
<div id="divCheckbox"  v-show="hasArrived">
  <button @click="tosend.Offset =tosend.Display"  >next </button>
  <button @click="tosend.Offset-=tosend.Display" v-if="tosend.Offset>=tosend.Display">back </button>
</div>

</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tosend: {
        Semester:"Fall",
        Year:"2022",
        StudentID:"",
        DateCreated:"",
        Classification:"",
        Major:"",
        FirstName:"",
        LastName:"",
        Display:25,
        Offset:0,
        ListofCourses:""
      },
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
      Addthis:"",
      hasArrived:false,
      tableStuff: [],
      countTable :0,
      hasTable:false
    };
  },
  methods:{
    Seeform(){
      var otherdic = {}
      for (var things in this.tosend){
         if(this.tosend[things] != "")
         {
           otherdic[things] = this.tosend[things]
         }
      }
      console.log(JSON.stringify(otherdic))
      axios
        .post("http://143.244.153.25:8004/Advising/All",JSON.stringify(otherdic), {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          //Perform Success Action
          if(res.data !="Invalid Advising filters")
          {
              
              this.tableStuff = res.data
              //for later how to display next
              this.countTable = this.tableStuff.length
              this.hasArrived = true
              this.hasTable =true
          }
          else{
              this.hasArrived = true
              this.hasTable = false
          }
          
          
        })
        .catch((error) => {
          // error.response.status Check status code
          console.log(error);
        })
        .finally(() => {
          //Perform action in always
          
        });
    }
  },
  watch:{
'tosend.Display':function(val){
   this.tosend.Display =val
   this.Seeform()
},
'tosend.Offset':function(val){
  this.tosend.Offset =val
  this.Seeform()
}
  }

};
</script>

<style  scoped>
button {
  background: #0b6dff;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
}
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #48a7a7;
}
.error {
  color: #ff0062;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
</style>