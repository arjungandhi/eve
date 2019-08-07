import React from 'react'
import { } from "semantic-ui-react"

export default class Task extends React.Component {

  constructor(props) {
    //make a blank articles list in state
    super(props)
  }

  componentDidMount() {
  }

  render() {
    return (<div>
      <ul>
        <li><Link to='/'>Tasks</Link></li>
        <li><Link to='/project/potato'>Potato Project</Link></li>
      </ul>
      <div />)
    }
    }
