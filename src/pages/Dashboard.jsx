import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";


function Dashboard(){

    return (

        <div>


            <Navbar />


            <Sidebar />


            <main>


                <h1>
                    Dashboard
                </h1>


                <h3>
                    Welcome to AI Task Management System
                </h3>


                <div>


                    <h2>
                        Documents
                    </h2>

                    <p>
                        Manage uploaded documents and semantic search.
                    </p>


                </div>



                <div>


                    <h2>
                        Tasks
                    </h2>

                    <p>
                        Create and manage assigned tasks.
                    </p>


                </div>


            </main>


        </div>

    );

}


export default Dashboard;