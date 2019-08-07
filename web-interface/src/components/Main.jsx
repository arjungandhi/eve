import React from 'react'
import {Button} from "semantic-ui-react"
import axios from 'axios'
import Content from './Content'
import { Link }from 'react-router-dom'

export default class Main extends React.Component {

  constructor(props) {
    //make a blank articles list in state
    super(props)
  }

  componentDidMount() {
    //get task from api.arjungandhi.com
    axios.post('https://api.arjungandhi.com/jaspr/task/sync', {}).then((response) => {
      sessionStorage.setItem('jaspr-tasks', response.body)
    }).catch(function(error) {
      // handle error
      console.log(error);
    })
  }

  render() {
    return (<div>
      <ul>
      <li><Link to='/'>Tasks</Link></li>
      <li><Link to='/project/potato'>Potato Project</Link></li>
      </ul>
    <Content/>
    </div>)
  }
}
