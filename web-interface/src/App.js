import React from "react";
import {render} from "react-dom";
import 'semantic-ui-css/semantic.min.css'
import {} from 'semantic-ui-react'
import Main from './components/Main.jsx'

const App = () => {
  return (<div >
    <Main/>
  </div>)
};
render(<App/>, document.getElementById("app"));
