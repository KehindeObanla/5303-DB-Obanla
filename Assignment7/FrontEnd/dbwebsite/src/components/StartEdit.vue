<template>
<h1 Edit {{ Title }} </h1>
<label for="CostAd">{{Value}}:</label><br />
<input type="text" id="CostAd" name="CostAd" v-model ="sendto">
<router-link :to="{name:{{togo}}, params:{ id: sendto}}">
       Submit  
</router-link>
</template>

<script>
export default {
  props: ["Title"],
  data(){
    return {
        Value :"",
        sendto :"",
        togo:""
    },
    beforeMount(){
      if(this.Title == "course")
      {
        this.Value= 'Crn'
        this.togo ="Editcourse"
      }
      else if(this.Title == "Student")
      {
        this.Value= 'Mnumber'
        this.togo ="Editstudent"
      }
      else if(this.Title == "Advising")
      {
        this.Value= 'Mnumber'
        this.togo ="EditAdvising"
      }

    }
};
</script>

<style>
</style>