import { useEffect, useState } from "react";
import API from "../api/axios";


function Tasks(){

    const [tasks,setTasks] = useState([]);


    const [title,setTitle] = useState("");

    const [description,setDescription] = useState("");

    const [assignedTo,setAssignedTo] = useState("");



    useEffect(()=>{

        getTasks();

    },[]);



    const getTasks = async()=>{

        try{

            const response = await API.get(
                "/tasks/"
            );


            setTasks(response.data);


        }
        catch(error){

            console.log(error);

        }

    };



    const createTask = async()=>{


        try{


            await API.post(

                `/tasks/?title=${title}&description=${description}&assigned_to=${assignedTo}`

            );


            alert(
                "Task created successfully"
            );


            getTasks();


            setTitle("");

            setDescription("");

            setAssignedTo("");


        }
        catch(error){

            console.log(error);

        }

    };



    return (

        <div>


            <h1>
                Task Management
            </h1>



            <h2>
                Create Task
            </h2>



            <input

                type="text"

                placeholder="Task title"

                value={title}

                onChange={
                    (e)=>setTitle(e.target.value)
                }

            />

            <br/><br/>



            <textarea

                placeholder="Description"

                value={description}

                onChange={
                    (e)=>setDescription(e.target.value)
                }

            />

            <br/><br/>



            <input

                type="number"

                placeholder="Assign User ID"

                value={assignedTo}

                onChange={
                    (e)=>setAssignedTo(e.target.value)
                }

            />


            <br/><br/>



            <button onClick={createTask}>

                Create Task

            </button>




            <hr/>




            <h2>
                All Tasks
            </h2>



            {

                tasks.map((task)=>(


                    <div key={task.id}>


                        <h3>
                            {task.title}
                        </h3>


                        <p>
                            {task.description}
                        </p>


                        <p>
                            Status:
                            {task.status}
                        </p>


                        <p>
                            Assigned To:
                            {task.assigned_to}
                        </p>


                        <hr/>


                    </div>


                ))

            }



        </div>

    );

}


export default Tasks;