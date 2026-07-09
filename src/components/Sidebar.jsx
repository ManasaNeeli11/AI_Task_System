import { Link } from "react-router-dom";


function Sidebar(){

    return (

        <div>


            <h3>
                Menu
            </h3>


            <Link to="/dashboard">
                Dashboard
            </Link>

            <br/>


            <Link to="/upload">
                Upload
            </Link>

            <br/>


            <Link to="/search">
                Search
            </Link>

            <br/>


            <Link to="/tasks">
                Tasks
            </Link>

            <br/>


            <Link to="/analytics">
                Analytics
            </Link>


        </div>

    );

}


export default Sidebar;