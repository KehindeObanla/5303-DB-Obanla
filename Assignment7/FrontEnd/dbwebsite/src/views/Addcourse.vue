<template>
  <div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('Seecourse')">See All Courses</button>
  </div>
  <form v-on:submit.prevent="Addcourse" class="Addcourses">
    <div ref="content">
      <h1>Enter Course</h1>
      
      <label for="Col">College(Abrv):</label><br />
      <input type="text"  list="Cols" v-model="tosend.Col" />
      <datalist  name="Col" id="Cols" required>
        <option v-for="item in Cols" :key="item" :value="item" />
      </datalist>

      <label for="Crn">Crn:</label><br />
      <input type="text" id="Crn" name="Crn" v-model="tosend.Crn" required />

      <label for="Subj">Subject(Abrv):</label><br />
      <input type="text"  list="Subj" v-model="tosend.Subj"/>
      <datalist name="Subj" id="Subj" required>
        <option v-for="item in Subjs" :key="item" :value="item" />
      </datalist>

      <label for="Crse">Course:</label><br />
      <input type="text" id="Crse" name="Crse" required v-model="tosend.Crse" />

      <label for="Sect">Section:</label><br />
      <input type="text" id="Sect" name="Sect" required v-model="tosend.Sect" />
      <label for="Title">Title:</label><br />
      <input
        type="text"
        id="Title"
        name="Title"
        required
        v-model="tosend.Title"
      />
      <label for="PrimaryInstructor">PrimaryInstructor:</label><br />
      <input
        type="text"
        id="PrimaryInstructor"
        name="PrimaryInstructor"
        required
        v-model="tosend.PrimaryInstructor"
      />
      <label for="Max">Max:</label><br />
      <input type="number" id="Max" name="Max" v-model="tosend.Max" />
      <label for="Curr">Current:</label><br />
      <input type="number" id="Curr" name="Curr" v-model="tosend.Curr" />
      <label for="Aval">Avalable:</label><br />
      <input type="number" id="Aval" name="Aval" v-model="tosend.Aval" />
      <label for="Days">Days:</label><br />
      <input type="text" id="Days" name="Days" v-model="tosend.Days" />
      <label for="Begin">Begin:</label><br />
      <input type="time" id="Begin" name="Begin" v-model="tosend.Begin" />
      <label for="End">End:</label><br />
      <input type="time" id="End" name="End" v-model="tosend.End" />

      <label for="Bldg">Buliding(Abrv):</label><br />
      <input type="text"  list="Bldg"  v-model="tosend.Bldg" />
      <datalist name="Bldg" id="Bldg">
        <option v-for="item in Bldgs" :key="item" :value="item" />
      </datalist>

      <label for="Room">Room Number:</label><br />
      <input type="text" id="Room" name="Room" v-model="tosend.Room" />

      <label for="year">Choose a Year:</label><br />
      <select name="year" id="year" required v-model="tosend.year">
        <option value="2021">2021</option>
        <option value="2022">2022</option>
      </select>

      <label for="Semester">Choose a Semester:</label><br />
      <select name="Semester" id="Semester" required v-model="tosend.Season">
        <option value="Fall">Fall</option>
        <option value="Spring">Spring</option>
        <option value="Summer1">Summer1</option>
        <option value="Summer2">Summer2</option>
      </select>
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
        Col:"",
        Crn: "",
        Subj:"",
        Crse: "",
        Sect: "",
        Title: "",
        PrimaryInstructor: "",
        Max: -1,
        Curr: -1,
        Aval: -1,
        Days: "",
        Begin: "",
        End: "",
         Bldg:"",
        Room: "",
        year: 0,
        Season: "",
      },
      passwordError: "",
      Cols: ["HH", "BA", "ED", "FA", "HM", "UN", "SE"],
       Subjs: [
          "ACCT",
          "AGBU",
          "AMUS",
          "ART",
          "ATRN",
          "BAAS",
          "BIOL",
          "BUAD",
          "CHEM",
          "CMPS",
          "COUN",
          "CRJU",
          "DNHY",
          "ECED",
          "ECON",
          "EDBE",
          "EDLE",
          "EDUC",
          "ENGL",
          "ENSC",
          "EPSY",
          "ETEC",
          "EXPH",
          "FINC",
          "FREN",
          "GEOG",
          "GEOS",
          "GERM",
          "GLBS",
          "GNMT",
          "GNSC",
          "HIST",
          "HSAD",
          "HSHS",
          "HUMN",
          "IDT",
          "KNES",
          "LSBA",
          "MATH",
          "MCOM",
          "MENG",
          "MGMT",
          "MIS",
          "MKTG",
          "MLSC",
          "MUSC",
          "MWSU",
          "NURS",
          "PETE",
          "PHIL",
          "PHYS",
          "POLS",
          "PSYC",
          "RADS",
          "READ",
          "RESP",
          "SOCL",
          "SOST",
          "SOWK",
          "SPAD",
          "SPAN",
          "SPCH",
          "SPED",
          "STAT",
          "STEM",
          "TECH",
          "THEA",
          "UGRO",
          "X21",
        ],
        Bldgs: [
          "BH",
          "BO",
          "BW",
          "CE",
          "CL",
          "CO",
          "CR",
          "DB",
          "FA",
          "FM",
          "HA",
          "LI",
          "MA",
          "MY",
          "OR",
          "PS",
          "PY",
          "SITE",
          "TC",
          "UNT",
          "VB",
        ],
    };
  },
  methods: {
    Addcourse() {
      console.log(this.tosend)
      axios
        .post(
          "http://143.244.153.25:8004/Addcourse/",
          JSON.stringify(this.tosend),
          { headers: { "Content-Type": "application/json" } }
        )
        .then((res) => {
          //Perform Success Action
          // JSON responses are automatically parsed.
          this.post = res.data;
          if (this.post["success"] == true) {
            this.reset();
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
  },
};
</script >

<style>

</style>