import React from 'react'
import {} from "semantic-ui-react"
import axios from 'axios'
import TaskPage from './TaskPage'

export default class Main extends React.Component {

  constructor(props) {
    //make a blank articles list in state
    super(props)
    this.state = {
      page : 'task'
    }
  }

  componentDidMount() {
    //get task from api.arjungandhi.com
    axios.post('https://api.arjungandhi.com/jaspr/task/sync', {})
    .then((response) => {
      sessionStorage.setItem('jaspr-tasks',response.body)

    }).catch(function(error) {
      // handle error
      console.log(error);

    })

  }

  render() {
    return (< div > < /div>)
      }
    }
