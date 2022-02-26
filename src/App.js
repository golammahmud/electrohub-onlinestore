import "./index.css";

import Home from "./components/pages/home";
import ApiContext from "./components/context/mycontext";
function App() {
  return (
    <div>
     <ApiContext> <Home /></ApiContext>
       
     
    </div>
  );
}

export default App;
