<template>
<div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('Seestudent')">See All Students</button>
  </div>
   <div v-show ="showMnumber">
     <form v-on:submit.prevent="getStudent" class="getStudents">
      <label for="CostAd">Enter Mnumber</label><br />
    <input type="text" id="CostAd" name="CostAd" v-model ="PMnumber">
    <div class="submit">
      <button>Submit</button>
    </div>
     </form>
   
    
  </div>
  <form v-on:submit.prevent="UpdateStudent" class="UpdateStudent" v-show="showform">
    <div ref="content">
      <h1>Enter Studnet info</h1>
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
        id="Mnumber"
        name="Mnumber"
        v-model="tosend.Mnumber"
        :placeholder="PMnumber"
        required
      /><br />

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

      <label for="Email">Email:</label><br />
      <input
        type="text"
        id="Email"
        name="Email"
        v-model="tosend.Email"
        :placeholder="PEmail"
      /><br />

      <label for="Gpa">Gpa:</label><br />
      <input
        type="text"
        id="Gpa"
        name="Gpa"
        v-model="tosend.Gpa"
        :placeholder="PGpa"
      /><br />

      <label for="GithubUname">Github username:</label>
      <input
        type="text"
        id="GithubUname"
        name="GithubUname"
        v-model="tosend.GithubUname"
        :placeholder="PGithubUname"
      />
    </div>
    <div v-if="passwordError" class="error">{{ passwordError }}</div>
    <div class="submit">
      <button>Submit form</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";
export default {
   data() {
    return {
      tosend: {
        Mnumber:"",
        FirstName:"",
        LastName:"",
        Classification:"",
        Email:"",
        Gpa:"",
        GithubUname:"",
      },
      passwordError: "",
      PMnumber:"",
      PFirstName:"No First Name",
      PLastName:"No Last Name",
      PClassification:"",
      PEmail:"No Email",
      PGpa:"No GPA",
      PGithubUname:"NO GitName",
      showform :false,
      showMnumber:true,
      answer :{},
      post:""
    };
  },
  methods: {
    UpdateStudent() {
      var otherdic = {}
      for (var things in this.tosend){
         if(this.tosend[things] != "")
         {
           otherdic[things] =this.tosend[things]
         }
      }
      console.log(otherdic)
      axios
        .patch(
          "http://143.244.153.25:8004/UpdateStudent",
          JSON.stringify(otherdic),
          { headers: { "Content-Type": "application/json" } }
        )
        .then((res) => {
          //Perform Success Action
          // JSON responses are automatically parsed.
          this.post = res.data;
          
          if (this.post["success"] == true) {
            this.reset();
            this.passwordError="Updated!!"
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
    reset() {
      this.post = false;
      for (let field in this.tosend) {
        this.tosend[field] = "";
      }
    },
    getStudent(){
      axios
        .get(
          "http://143.244.153.25:8004/student/Mnumber/"+this.PMnumber)
        .then((res) => {
          //Perform Success Action
          // JSON responses are automatically parsed.
         
          this.answer = res.data[0]
           console.log(this.answer)
          if (res.data != "Invalid Mnumber") {
             if(this.answer.FirstName!="")
            {
              this.PFirstName = this.answer.FirstName
            }
           if(this.answer.LastName!="")
            {
              this.PLastName = this.answer.LastName
            }
            if(this.answer.Mnumber!="")
            {
              this.PMnumber = this.answer.Mnumber
              this.tosend.Mnumber=this.PMnumber
            }
            if(this.answer.Email!="")
            {
               this.PEmail = this.answer.Email
            }
            if(this.answer.GPA!="")
            {
              this.PGpa = this.answer.GPA
            }
            if(this.answer.GitHubUname!="")
            {
              this.PGithubUname = this.answer.GitHubUname
            }
            if(this.answer.Classification!="")
            {
              this.PClassification = this.answer.Classification
            }
            this.showMnumber=false
            this.showform = true
            this.tosend.Classification = this.PClassification
          } else {
            this.passwordError = "Invalid Mnumber"
            
          }
        })
        .catch((error) => {
          // error.response.status Check status code
          this.passwordError = error.statuscode;
        })
        .finally(() => {
          //Perform action in always
          console.log("final")
        });
    }
  },
}
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