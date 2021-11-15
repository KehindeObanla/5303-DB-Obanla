<template>
  <div>
    <ul class="demo">
      <li>
        <router-link to="/Addcourse"> Add Course</router-link>
      </li>
      <li>
        <router-link to="/AddStudent"> Add Student</router-link>
      </li>
      <li>
        <router-link to="/AddAdvising"> Add Advising form</router-link>
      </li>
      <li>
        <router-link to="/Editcourse">Edit Course</router-link>
      </li>
      <li>
        <router-link to="/Editstudent"> Edit Student</router-link>
      </li>
      <li>
        <router-link to="/EditAdvising"> Edit Advising form</router-link>
      </li>
      <li>
        <router-link to="/Seecourse"> See Course</router-link>
      </li>
      <li>
        <router-link to="/Seestudent"> See Student</router-link>
      </li>
      <li>
        <router-link to="/SeeAdvising"> See Advising</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Main",
};
</script>

<style>
ul {
  list-style-type: none;
  padding: 0;
  border: 1px solid #ddd;
}

ul li {
  padding: 8px 16px;
  border-bottom: 1px solid #ddd;
}

ul li:last-child {
  border-bottom: none;
}
ul .demo {
  text-align: left;
}
</style>