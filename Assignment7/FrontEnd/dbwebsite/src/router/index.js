import { createRouter, createWebHistory } from 'vue-router'
import Main from '../views/mainpage.vue'
import notfound from '../views/notfound.vue'
import AddAdvising from '../views/Addadvsing.vue'
import AddStudent from '../views/AddStudent.vue'
import EditAdvising from '../views/EditAdvising.vue'
import Editcourse from '../views/Editcourse.vue'
import Editstudent from '../views/Editstudent.vue'
import SeeAdvising from '../views/SeeAdvising.vue'
import Seecourse from '../views/Seecourse.vue'
import Seestudent from '../views/Seestudent.vue'
import Addcourse from '../views/Addcourse.vue'
const routes = [
  {
    path:'/',
    redirect:'/mainpage',
    
},
  {
    path:'/mainpage',
    name:'Main',
    component: Main
  },
  //catch all 404
  {
    path: '/:catchAll(.*)',
    name: 'notfound',
    component: notfound,

},
{
  path: '/AddAdvising',
  name: 'AddAdvising',
  component: AddAdvising
},
{
  path: '/Addcourse',
  name: 'Addcourse',
  component: Addcourse
},
{
  path: '/AddStudent',
  name: 'AddStudent',
  component: AddStudent
},
{
  path: '/EditAdvising',
  name: 'EditAdvising',
  component: EditAdvising
},
{
  path: '/Editcourse',
  name: 'Editcourse',
  component: Editcourse
},
{
  path: '/Editstudent',
  name: 'Editstudent',
  component: Editstudent
},
{
  path: '/SeeAdvising',
  name: 'SeeAdvising',
  component: SeeAdvising
},
{
  path: '/Seecourse',
  name: 'Seecourse',
  component: Seecourse
},
{
  path: '/Seestudent',
  name: 'Seestudent',
  component: Seestudent
},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
