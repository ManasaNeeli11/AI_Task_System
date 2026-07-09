import {
BrowserRouter,
Routes,
Route
} from "react-router-dom";


import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Search from "./pages/Search";
import Tasks from "./pages/Tasks";
import Analytics from "./pages/Analytics";

import ProtectedRoute from "./components/ProtectedRoute";



function App(){


return (

<BrowserRouter>

<Routes>


<Route
path="/"
element={<Login/>}
/>



<Route

path="/dashboard"

element={

<ProtectedRoute>

<Dashboard/>

</ProtectedRoute>

}

/>



<Route
path="/upload"
element={
<ProtectedRoute>
<Upload/>
</ProtectedRoute>
}
/>



<Route
path="/search"
element={
<ProtectedRoute>
<Search/>
</ProtectedRoute>
}
/>



<Route
path="/tasks"
element={
<ProtectedRoute>
<Tasks/>
</ProtectedRoute>
}
/>



<Route
path="/analytics"
element={
<ProtectedRoute>
<Analytics/>
</ProtectedRoute>
}
/>


</Routes>


</BrowserRouter>


)

}


export default App;