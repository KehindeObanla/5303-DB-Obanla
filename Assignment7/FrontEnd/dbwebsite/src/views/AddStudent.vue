<template>
  <div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('Seestudent')">See All Students</button>
  </div>
  <form v-on:submit.prevent="Addstudent" class="Addstudents">
    <div ref="content">
      <h1>Enter Studnet info</h1>
      <label for="Fname">FirstName:</label><br />
      <input
        type="text"
        id="Fname"
        name="Fname"
        v-model="tosend.FirstName"
        required
      />

      <label for="Lname">LastName:</label><br />
      <input
        type="text"
        id="Lname"
        name="Lname"
        v-model="tosend.LastName"
        required
      /><br />

      <label for="Mnumber">Mnumber:</label><br />
      <input
        type="text"
        id="Mnumber"
        name="Mnumber"
        required
        v-model="tosend.Mnumber"
      /><br />

      <label for="Classification">Choose a Classification:</label>
      <select
        name="Classification"
        id="Classification"
        v-model="tosend.Classification"
      >
        <option value="Freshman">Freshman</option>
        <option value="Sophomore">Sophomore</option>
        <option value="junior">junior</option>
        <option value="Senior">Senior</option>
      </select>

      <label for="Email">Email:</label><br />
      <input
        type="Email"
        id="Email"
        name="Email"
        v-model="tosend.Email"
      /><br />

      <label for="Gpa">Gpa:</label><br />
      <input type="text" id="Gpa" name="Gpa" v-model="tosend.Gpa" /><br />

      <label for="GithubUname">Github username:</label>
      <input
        type="text"
        id="GithubUname"
        name="GithubUname"
        v-model="tosend.GithubUname"
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
        Mnumber: "",
        FirstName: "",
        LastName: "",
        Classification: "",
        Email: "",
        Gpa: -1,
        GithubUname: "",
      },
      passwordError: "",
    };
  },
  methods: {
    Addstudent() {
      axios
        .post(
          "http://143.244.153.25:8004/AddStudent/",
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