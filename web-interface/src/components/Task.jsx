import React from 'react'
import {} from "semantic-ui-react"

export default class Task extends React.Component {

    constructor(props) {
      //make a blank articles list in state
      super(props)
    }

    componentDidMount() {
      console.log('task')

    }

    render() {
      return ( < p > I is the Task Page < /p>)
      }
    }
