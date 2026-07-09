import { useEffect, useState } from "react";
import API from "../api/axios";


function Analytics(){

    const [data,setData] = useState(null);



    useEffect(()=>{

        getAnalytics();

    },[]);



    const getAnalytics = async()=>{


        try{

            const response = await API.get(
                "/analytics/"
            );


            setData(response.data);


        }
        catch(error){

            console.log(error);

        }

    };



    return (

        <div>


            <h1>
                Analytics Dashboard
            </h1>



            {
                data ? (

                    <div>


                        <h2>
                            Overview
                        </h2>



                        <p>
                            Total Documents:
                            {data.total_documents}
                        </p>



                        <p>
                            Total Tasks:
                            {data.total_tasks}
                        </p>



                        <p>
                            Total Activity:
                            {data.total_activity}
                        </p>



                        <hr/>


                        <h2>
                            Recent Activity
                        </h2>



                        {

                            data.recent_activity.map(
                                (activity)=>(

                                    <div key={activity.id}>


                                        <p>

                                            Action:
                                            {activity.action}

                                        </p>


                                        <p>

                                            User:
                                            {activity.user_id}

                                        </p>


                                        <p>

                                            Date:
                                            {activity.created_at}

                                        </p>


                                        <hr/>

                                    </div>

                                )
                            )

                        }



                    </div>


                ):(

                    <p>
                        Loading analytics...
                    </p>

                )

            }



        </div>

    );

}


export default Analytics;