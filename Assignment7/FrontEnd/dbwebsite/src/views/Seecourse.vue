<template>
  <div class ="teststile">
      <button @click="$router.push('mainpage')">Home</button>
      <button @click="$router.push('Editcourse')">Edit course  schedule</button>
    </div>
    <br><br>
   <form v-on:submit.prevent="Seecourse" class="Seecourses">
    <div ref="content">
		<table class ="help">
			<tr>
				<td>
					Semester<select name="Semester" id="Semester"  v-model="tosend.Season">
						<option value="Fall">Fall</option>
						<option value="Spring">Spring</option>
						<option value="Summer1">Summer1</option>
						<option value="Summer2">Summer2</option>
					  </select>
				   </td>
				<td> College<input type="text"  list="Cols" v-model="tosend.Col" /> 
				 <datalist  name="Col" id="Cols" >
				   <option v-for="item in Cols" :key="item" :value="item" />
				 </datalist> </td>
				 
				 <td>
					 Subject<input type="text"  list="Subj" v-model="tosend.Subj"/>
					 <datalist name="Subj" id="Subj" >
					   <option v-for="item in Subjs" :key="item" :value="item" />
					 </datalist>
				 </td>
				 <td>
					 Buliding<input type="text"  list="Bldg"  v-model="tosend.Bldg" />
					 <datalist name="Bldg" id="Bldg">
					 <option v-for="item in Bldgs" :key="item" :value="item" />
					 </datalist>
				 </td>
				 <td>
					 Year<select name="year" id="year"  v-model="tosend.year">
						 <option value="2021">2021</option>
						 <option value="2022">2022</option>
					   </select>
				 </td>
			</tr>
			<tr>
			 <td>
				 Course<input type="text" id="Crse" name="Crse"  v-model="tosend.Crse" />
			 </td>
			 <td>
				 Section<input type="text" id="Sect" name="Sect"  v-model="tosend.Sect" />
			 </td>
			 <td>
				 Title: <input
				 type="text"
				 id="Title"
				 name="Title"
				 v-model="tosend.Title"
			   />
			 </td>
			 <td>
				 PrimaryInstructor<input
				 type="text"
				 id="PrimaryInstructor"
				 name="PrimaryInstructor"
				 v-model="tosend.PrimaryInstructor"
			   />
			 </td>
			</tr>
			<tr>
				 <td>
					 Crn:<input type="text" id="Crn" name="Crn" v-model="tosend.Crn"/>
           </td>
				 <td>
					 Max <input type="number" id="Max" name="Max" v-model="tosend.Max"/>
				 </td>
				 <td> Current<input type="number" id="Curr" name="Curr" v-model="tosend.Curr" /></td>
				 <td> Avalable <input type="number" id="Aval" name="Aval" v-model="tosend.Aval" /></td>
			</tr>
			<tr>
			 <td>
				 Days<input type="text" id="Days" name="Days" v-model="tosend.Days" /><br>
			 </td>
			 <td>
				 Begin <input type="time" id="Begin" name="Begin" v-model="tosend.Begin" />
			 </td>
			 <td>End<input type="time" id="End" name="End" v-model="tosend.End" /></td>
			 <td>Room<input type="text" id="Room" name="Room" v-model="tosend.Room" /></td>
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
    <th>Col</th>
    <th>Crn</th>
    <th>Subj</th>
    <th>Crse</th>
    <th>Sect</th>
    <th>Title</th>
    <th>PrimaryInstructor</th>
    <th>Max</th>
    <th>Curr</th>
    <th>Aval</th>
    <th>Days</th>
    <th>Begin</th>
    <th>End</th>
    <th>Bldg</th>
    <th>Room</th>
    <th>year</th>
    <th>Semester</th>
  </tr>
    <tr v-for="item in tableStuff" v-show ="hasTable"> 
      <th>{{item.Col}}</th>
      <th>{{item.Crn}}</th>
      <th>{{item.Subj}}</th>
      <th>{{item.Crse}}</th>
      <th>{{item.Sect}}</th>
      <th>{{item.Title}}</th>
      <th>{{item.PrimaryInstructor}}</th>
      <th>{{item.Max}}</th>
      <th>{{item.Curr}}</th>
      <th>{{item.Aval}}</th>
      <th>{{item.Days}}</th>
      <th>{{item.Begin}}</th>
      <th>{{item.End}}</th>
      <th>{{item.Bldg}}</th>
      <th>{{item.Room}}</th>
      <th>{{item.year}}</th>
      <th>{{item.Season}}</th>
    </tr>
   </table>
  </div>
</template>

<script>
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
  methods:{
    Seecourse(){
      
    }
  }
}
</script>

<style>
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

.done th, td {
  text-align: left;
  padding: 8px;
}

.done tr:nth-child(even) {
  background-color: #48a7a7;
}
.error {
  color: #ff0062;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
</style>