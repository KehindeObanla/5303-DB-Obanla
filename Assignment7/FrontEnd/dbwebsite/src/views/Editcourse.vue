<template>
  <div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('Seecourse')">See All Courses</button>
  </div>
  <div v-show="showMnumber">
    <form v-on:submit.prevent="getadvsing" class="getadvsing">
      <label for="CostAd">Enter CRN</label><br />
      <input type="text" id="CostAd" name="CostAd" v-model="PCrn" />
      <div class="submit">
        <button>Submit</button>
      </div>
    </form>
  </div>
  <form
    v-on:submit.prevent="Updatecourse"
    class="Updatecourse"
    v-show="showform"
  >
    <div ref="content">
      <h1>Enter Course</h1>

      <label for="Col">College(Abrv):</label><br />
      <input type="text" list="Cols" v-model="PCol" />
      <datalist name="Col" id="Cols">
        <option v-for="item in Cols" :key="item" :value="item" />
      </datalist>

      <label for="Crn">Crn:</label><br />
      <input
        type="text"
        id="Crn"
        name="Crn"
        v-model="tosend.Crn"
        :placeholder="PCrn"
      />

      <label for="Subj">Subject(Abrv):</label><br />
      <input type="text" list="Subj" v-model="PSubj" />
      <datalist name="Subj" id="Subj">
        <option v-for="item in Subjs" :key="item" :value="item" />
      </datalist>

      <label for="Crse">Course:</label><br />
      <input
        type="text"
        id="Crse"
        name="Crse"
        v-model="tosend.Crse"
        :placeholder="PCrse"
      />

      <label for="Sect">Section:</label><br />
      <input
        type="text"
        id="Sect"
        name="Sect"
        v-model="tosend.Sect"
        :placeholder="PSect"
      />
      <label for="Title">Title:</label><br />
      <input
        type="text"
        id="Title"
        name="Title"
        :placeholder="PTitle"
        v-model="tosend.Title"
      />
      <label for="PrimaryInstructor">PrimaryInstructor:</label><br />
      <input
        type="text"
        id="PrimaryInstructor"
        name="PrimaryInstructor"
        :placeholder="PPrimaryInstructor"
        v-model="tosend.PrimaryInstructor"
      />
      <label for="Max">Max:</label><br />
      <input
        type="number"
        id="Max"
        name="Max"
        v-model="tosend.Max"
        :placeholder="PMax"
      />
      <label for="Curr">Current:</label><br />
      <input
        type="number"
        id="Curr"
        name="Curr"
        v-model="tosend.Curr"
        :placeholder="PCurr"
      />
      <label for="Aval">Avalable:</label><br />
      <input
        type="number"
        id="Aval"
        name="Aval"
        v-model="tosend.Aval"
        :placeholder="PAval"
      />
      <label for="Days">Days:</label><br />
      <input
        type="text"
        id="Days"
        name="Days"
        v-model="tosend.Days"
        :placeholder="PDays"
      />
      <label for="Begin">Begin:</label><br />
      <input type="time" id="Begin" name="Begin" v-model="PBegin" />
      <label for="End">End:</label><br />
      <input type="time" id="End" name="End" v-model="PEnd" />

      <label for="Bldg">Buliding(Abrv):</label><br />
      <input type="text" list="Bldg" v-model="PBldg" />
      <datalist name="Bldg" id="Bldg">
        <option v-for="item in Bldgs" :key="item" :value="item" />
      </datalist>

      <label for="Room">Room Number:</label><br />
      <input
        type="text"
        id="Room"
        name="Room"
        v-model="tosend.Room"
        :placeholder="PRoom"
      />

      <label for="year">Choose a Year:</label><br />
      <select name="year" id="year" v-model="Pyear">
        <option value="2021">2021</option>
        <option value="2022">2022</option>
      </select>

      <label for="Semester">Choose a Semester:</label><br />
      <select name="Semester" id="Semester" v-model="PSeason">
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
        Col: "",
        Crn: "",
        Subj: "",
        Crse: "",
        Sect: "",
        Title: "",
        PrimaryInstructor: "",
        Max: "",
        Curr: "",
        Aval: "",
        Days: "",
        Begin: "",
        End: "",
        Bldg: "",
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
      PCol: "",
      PCrn: "",
      PSubj: "",
      PCrse: "NO course",
      PSect: "NO Section",
      PTitle: "NO Title",
      PPrimaryInstructor: "NO proffersor",
      PMax: "NO Max",
      PCurr: "NO CURR",
      PAval: "NO Availabel",
      PDays: "NO Days",
      PBegin: "",
      PEnd: "",
      PBldg: "",
      PRoom: "NO ROOM",
      Pyear: " ",
      PSeason: "",
      showform: false,
      showMnumber: true,
      answer: {},
      post: "",
    };
  },
  methods: {
    getadvsing() {
      axios
        .get("http://143.244.153.25:8004/courses/Crn/" + this.PCrn)
        .then((res) => {
          this.answer = res.data[0];
          console.log(res.data);
          console.log(this.answer);
          if (res.data != "invalid CRN") {
            if (this.answer.Col != "") {
              this.PCol = this.answer.Col;
            }
            if (this.answer.Crn != "") {
              this.PCrn = this.answer.Crn;
              this.tosend.Crn = this.PCrn;
            }
            if (this.answer.Subj != "") {
              this.PSubj = this.answer.Subj;
            }
            if (this.answer.Crse != "") {
              this.PCrse = this.answer.Crse;
            }
            if (this.answer.Sect != "") {
              this.PSect = this.answer.Sect;
            }
            if (this.answer.Title != "") {
              this.PTitle = this.answer.Title;
            }
            if (this.answer.PrimaryInstructor != "") {
              this.PPrimaryInstructor = this.answer.PrimaryInstructor;
            }
            if (this.answer.Max != "") {
              this.PMax = this.answer.Max;
            }
            if (this.answer.Curr != "") {
              this.PCurr = this.answer.Curr;
            }
            if (this.answer.Aval != "") {
              this.PAval = this.answer.Aval;
            }
            if (this.answer.Days != "") {
              this.PDays = this.answer.Days;
            }
            if (this.answer.Begin != "") {
              this.PBegin = this.answer.Begin;
            }
            if (this.answer.End != "") {
              this.PEnd = this.answer.End;
            }
            if (this.answer.Bldg != "") {
              this.PBldg = this.answer.Bldg;
            }
            if (this.answer.Room != "") {
              this.PRoom = this.answer.Room;
            }
            if (this.answer.year != "") {
              this.Pyear = this.answer.year;
            }
            if (this.answer.Season != "") {
              this.PSeason = this.answer.Season;
            }
            this.showMnumber = false;
            this.showform = true;
            this.tosend.Col = this.PCol;
            this.tosend.Subj = this.PSubj;
            this.tosend.Begin = this.PBegin;
            this.tosend.End = this.PEnd;
            this.tosend.Bldg = this.PBldg;
            this.tosend.year = this.Pyear;
            this.tosend.Season = this.PSeason;
          } else {
            this.passwordError = "invalid CRN";
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
    Updatecourse() {
      this.tosend.Col = this.PCol;
      this.tosend.Subj = this.PSubj;
      this.tosend.Begin = this.PBegin;
      this.tosend.End = this.PEnd;
      this.tosend.Bldg = this.PBldg;
      this.tosend.year = this.Pyear;
      this.tosend.Season = this.PSeason;
      var otherdic = {};
      for (var things in this.tosend) {
        if (this.tosend[things] != "") {
          otherdic[things] = this.tosend[things];
        }
      }
      console.log(otherdic);
      axios
        .patch(
          "http://143.244.153.25:8004/Updatecourse",
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
</script >

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