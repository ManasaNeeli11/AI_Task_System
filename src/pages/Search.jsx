import { useState } from "react";
import API from "../api/axios";


function Search(){

    const [query, setQuery] = useState("");

    const [results, setResults] = useState([]);

    const [loading, setLoading] = useState(false);



    const searchDocuments = async()=>{


        if(!query){

            return;

        }


        try{

            setLoading(true);


            const response = await API.get(
                `/search/?query=${query}`
            );


            setResults(response.data);


        }
        catch(error){

            console.log(error);

            setResults([]);

        }
        finally{

            setLoading(false);

        }

    };



    return (

        <div>


            <h1>
                Semantic Search
            </h1>



            <input

                type="text"

                placeholder="Search documents"

                value={query}

                onChange={
                    (e)=>setQuery(e.target.value)
                }

            />



            <button onClick={searchDocuments}>

                Search

            </button>



            {
                loading && (

                    <p>
                        Searching...
                    </p>

                )
            }



            <h2>
                Results
            </h2>



            {

                results.length === 0 && !loading && (

                    <p>
                        No results found
                    </p>

                )

            }



            {
                results.map((item,index)=>(


                    <div key={index}>


                        <h3>

                            Result {index + 1}

                        </h3>



                        {
                            item.filename && (

                                <p>

                                    <b>
                                        File:
                                    </b>

                                    {item.filename}

                                </p>

                            )
                        }




                        {
                            item.content && (

                                <p>

                                    <b>
                                        Content:
                                    </b>

                                    {item.content}

                                </p>

                            )
                        }




                        {
                            item.text && (

                                <p>

                                    <b>
                                        Text:
                                    </b>

                                    {item.text}

                                </p>

                            )
                        }




                        {
                            item.score && (

                                <p>

                                    <b>
                                        Similarity:
                                    </b>

                                    {item.score}

                                </p>

                            )
                        }



                        <hr/>


                    </div>


                ))
            }



        </div>

    );

}


export default Search;