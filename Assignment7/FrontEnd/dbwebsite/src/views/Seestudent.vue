<template>
  <div>
    <button @click="$router.push('mainpage')">Home</button>
    <button @click="$router.push('Editstudent')">Edit course schedule</button>
  </div>
  <br /><br />

  <form v-on:submit.prevent="SeeStudent" class="SeeStudent">
    <div ref="content">
      <table class="help">
        <tr>
          <td>
            FirstName<input
              type="text"
              id="FirstName"
              name="FirstName"
              v-model="tosend.FirstName"
            />
          </td>
          <td>
            LastName<input
              type="text"
              id="LastName"
              name="LastName"
              v-model="tosend.LastName"
            />
          </td>
          <td>
            Mnumber<input
              type="text"
              id="Mnumber"
              name="Mnumber"
              v-model="tosend.Mnumber"
            />
          </td>
          <td>
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
          </td>
        </tr>
        <tr>
          <td>
            Display<select name="Display" id="Display" v-model="tosend.Display">
              <option value="25">25</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </td>
          <td>
            GPA <input type="number" id="Gpa" name="Gpa" v-model="tosend.Gpa" step="0.01" />
          </td>
          <td>
            GpaEval<select name="GPAL" id="GPAL" v-model="tosend.GPAL">
               <option value="" selected ></option>
              <option value="0">Greater</option>
              <option value="1">Less</option>
              <option value="2">Equal</option>
            </select>
          </td>
        </tr>
      </table>
    </div>
    <div class="submit">
      <button>GO</button>
    </div>
  </form>
   <div ref="tableadd" id ="tableadd" >
   <table v-show="hasArrived" class ="doneTable">
    <tr>
    <th>FirstName</th>
    <th>LastName</th>
    <th>Mnumber</th>
    <th>Classification</th>
    <th>Email</th>
    <th>Gpa</th>
    <th>Github name</th>
  </tr>
    <tr v-for="item in tableStuff" v-show ="hasTable"> 
      <th>{{item.FirstName}}</th>
      <th>{{item.LastName}}</th>
      <th>{{item.Mnumber}}</th>
      <th>{{item.Classification}}</th>
      <th>{{item.Email}}</th>
      <th>{{item.GPA}}</th>
      <th>{{item.GitHubUname}}</th>

    </tr>
   </table>
  </div>
  <div id="divCheckbox" v-show="hasArrived">
    <button @click="tosend.Offset = tosend.Display">next</button>
    <button
      @click="tosend.Offset -= tosend.Display"
      v-if="tosend.Offset >= tosend.Display"
    >
      back
    </button>
  </div>
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
        Gpa: 0,
        GPAL:"",
        Display:25,
        offset:0
      },
      hasArrived:false,
      tableStuff: [],
      countTable :0,
      hasTable:false
      
    };
  },
    methods:{
    SeeStudent(){
      var otherdic = {}
      var count =0
      for (var things in this.tosend)
      {
         if(this.tosend[things] != "")
         {
           otherdic[things] = this.tosend[things]
           count++
         }
      }
      
      if(count ==1 && "Display" in otherdic)
      {
        
        axios
        .get("http://143.244.153.25:8004/student").then((res) => {
          //Perform Success Action
          if(res.data !="invalid subject")
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
      else{
         
        axios
        .post("http://143.244.153.25:8004/filterstudent",JSON.stringify(otherdic), {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          //Perform Success Action
          if(res.data !="Invalid student filters")
          {
              console.log("fuck")
              
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
      
    }
  },
   watch:{
'tosend.Display':function(val){
   this.tosend.Display =val
   this.Seecourse()
},
'tosend.Offset':function(val){
  this.tosend.Offset =val
  this.Seecourse()
}
  }

}
</script>

<style scoped>
button {
  background: #0b6dff;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
}
.doneTable {
  border-collapse: collapse;
  width: 100%;
}

.doneTable th, .doneTable td{
  text-align: left;
  padding: 8px;
  border: 1px solid black;
}
</style>