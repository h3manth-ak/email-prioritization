import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import './App.css'

import Navbar from "./components/Navbar";
import HighPriority from "./Pages/HighPriority";
import MediumPriority from "./Pages/MediumPriority";
import LowPriority from "./Pages/LowPriority";
import Spam from "./Pages/Spam";

function App() {
  

  return (
    <>
      <div className="backside">
      <Router>
      <Navbar />
        <Routes>
          <Route path="/" element={<HighPriority />} />
          <Route path="/med" element={<MediumPriority />} />
          <Route path="/low" element={<LowPriority />} />
          <Route path="/spam" element={<Spam />} />
        </Routes>
        {/* <Footer /> */}
      </Router>

      </div>
        
    </>
  )
}

export default App
