import './App.css';
import Login from '../src/pages/auth/Login';
import SignUp from './pages/auth/SignUp';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Navbar from './pages/Navbar/Navbar';

function App() {
  return (
    <Router>
    <div className="App">
      <Navbar/>
    <Switch>
      <Route exact path="/"><Login/></Route>
      <Route path="/SignUp"><SignUp/></Route>
      </Switch>
    </div>
    </Router>
  );
}

export default App;