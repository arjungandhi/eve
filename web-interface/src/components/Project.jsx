import React from 'react'
import {} from "semantic-ui-react"


export default class Project extends React.Component {

    constructor(props) {
      super(props)
    }

    componentDidMount() {
      console.log('Project:'+this.props.match.params.name)
    }

    render() {
      return ( < div > Hi I 'm the Project Page I have Represent the Proejct:{this.props.match.params.name}< /div>)
      }
    }
