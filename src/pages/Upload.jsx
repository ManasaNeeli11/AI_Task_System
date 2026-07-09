import { useState } from "react";
import API from "../api/axios";


function Upload(){

    const [file,setFile] = useState(null);
    const [message,setMessage] = useState("");



    const uploadFile = async()=>{

        if(!file){

            setMessage("Please select a file");

            return;

        }


        const formData = new FormData();


        formData.append(
            "file",
            file
        );


        try{


            const response = await API.post(
                "/documents/upload",
                formData,
                {
                    headers:{
                        "Content-Type":"multipart/form-data"
                    }
                }
            );


            setMessage(
                "File uploaded successfully"
            );


            console.log(response.data);


        }
        catch(error){

            console.log(error);

            setMessage(
                "Upload failed"
            );

        }

    }



    return (

        <div>

            <h1>
                Upload Document
            </h1>


            <input

                type="file"

                onChange={
                    (e)=>setFile(e.target.files[0])
                }

            />


            <br/><br/>


            <button onClick={uploadFile}>

                Upload

            </button>


            <p>
                {message}
            </p>


        </div>

    );

}


export default Upload;