<template>
  <div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('SeeAdvising')">See All Advising forms</button>
  </div>
  <form v-on:submit.prevent="doboth" class="Addadvsing">
    <div ref="content">
      <h1>Enter Advising Form</h1>
      <label for="Fname">FirstName:</label><br />
      <input type="text" id="Fname" name="Fname" v-model="tosend.FirstName" />

      <label for="Lname">LastName:</label><br />
      <input
        type="text"
        id="Lname"
        name="Lname"
        v-model="tosend.LastName"
      /><br />

      <label for="Mnumber">Mnumber:</label><br />
      <input
        type="text"
        id="StudentID"
        name="StudentID"
        required
        v-model="tosend.StudentID"
      /><br />
      <label for="Semester">Choose a Semester:</label>
      <select name="Semester" id="Semester" required v-model="tosend.Semester">
        <option value="Fall">Fall</option>
        <option value="Spring">Spring</option>
        <option value="Summer1">Summer1</option>
        <option value="Summer2">Summer2</option>
      </select>

      <label for="year">Choose a Year:</label>
      <select name="year" id="year" required v-model="tosend.Year">
        <option value="2021">2021</option>
        <option value="2022">2022</option>
      </select>

      <label for="Classification">Choose a Classification:</label>
      <select
        name="Classification"
        id="Classification"
        required
        v-model="tosend.Classification"
      >
        <option value="Freshman">Freshman</option>
        <option value="Sophomore">Sophomore</option>
        <option value="junior">junior</option>
        <option value="Senior">Senior</option>
      </select>

      <label for="Major">Major:</label><br />
      <input type="text" id="Major" name="Major" v-model="tosend.Major" /><br />

      <label for="ListofCourses">ListofCourses:</label><br />
      <input
        type="text"
        id="ListofCourses"
        name="ListofCourses"
        required
        v-model="tosend.ListofCourses"
      /><br />

      <label for="DateCreated">DateCreated:</label>
      <input
        type="date"
        id="DateCreated"
        name="DateCreated"
        required
        v-model="tosend.DateCreated"
      />
    </div>
    <div v-if="passwordError" class="error">{{ passwordError }}</div>
    <div id="addstuff" ref="addstuff"></div>
    <div class="submit">
      <button>Submit form</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";
import { jsPDF } from "jspdf";
import * as html2canvas from "html2canvas";
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
    };
  },
  methods: {
    doboth() {
      this.getCrn();
      this.getData();
    },
    getData() {
      axios
        .post(
          "http://143.244.153.25:8004/AddForm/",
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
      for (let field in this.htmldoc) {
        this.htmldoc[field] = "";
      }
    },
    download() {
      try {
        let pdfRef = this.$refs.content;

        html2canvas(pdfRef).then((canvas) => {
          let pdfImage = canvas.toDataURL("image/jpeg", 1.0);
          let second = this.image;
          let pdf = new jsPDF("l", "mm", "a4");
          pdf.addImage(pdfImage, "JPEG", 10, 10, 170, 180);
          pdf.addPage("p");
          pdf.addImage(second, "JPEG", 10, 10, 170, 180);
          pdf.html(this.htmldoc);
          pdf.save("Advisning.pdf");
        });
      } catch (error) {
        console.log(error);
      }
    },
    getCrn() {
      var listed = this.tosend.ListofCourses;
      var array = listed.split(",");

      axios
        .post("http://143.244.153.25:8004/maketable", JSON.stringify(array), {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          //Perform Success Action
          // JSON responses are automatically parsed.

          this.htmldoc = res.data;
          this.$refs.addstuff.innerHTML = this.htmldoc;
        })
        .catch((error) => {
          // error.response.status Check status code
          console.log(error);
        })
        .finally(() => {
          //Perform action in always
          this.createimage();
          this.download();
        });
    },
    createimage() {
      let pdfRef = this.$refs.addstuff;
      html2canvas(pdfRef, {
        height: window.outerHeight + window.innerHeight,
        windowHeight: window.outerHeight + window.innerHeight,
        scrollY: -window.scrollY,
      }).then((canvas) => {
        let pdfImage = canvas.toDataURL("image/jpeg", 1.0);
        this.image = pdfImage;
      });
    },
  },
};
</script>

<style scoped >
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