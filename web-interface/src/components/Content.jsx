import React from 'react'
import { } from "semantic-ui-react"
import { Route, Switch } from 'react-router-dom'
import Task from './Task.jsx'
import Project from './Project.jsx'

export default class Content extends React.Component {

  constructor(props) {
    //make a blank articles list in state
    super(props)
    this.state = {}
  }

  componentDidMount() { }

  render() {
    return (<Switch>
      <Route exact path='/' component={Task} />
      <Route path='/project/:name' component={Project} />
    </Switch>)
  }
}
