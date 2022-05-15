import './App.css';
import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";

import Navbar from "./components/Navbar";
import Projects from "./components/Projects";
import Placeholder from "./components/Placeholder";
import axios from "axios";

const WebFont = require('webfontloader');

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      projects: [],
      tasks: [],
      selected_project: 'initial',
      render: false,
    }
  }

  async loadData() {
    const headers = {
      'Content-Type': 'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='
    }

    let projects;
    await axios.get('http://127.0.0.1:8000/projects', {headers}).then(response => {
      projects = response.data;
    }).catch(error => {
      console.log(error)
    })

    let tasks;
    await axios.get('http://127.0.0.1:8000/tasks', {headers}).then(response => {
      tasks = response.data;
    }).catch(error => {
      console.log(error)
    })

    this.setState({projects, tasks, render: true})
  }

  selectProject(id) {
    this.setState({selected_project: id})
  }

  componentDidMount() {
    WebFont.load({
      google: {
        families: ['Roboto', 'Merriweather', 'Oswald']
      }
    })
    this.loadData()
  }

  render() {
    // console.log(this.state)
    return (<div>
      {this.state.render && <BrowserRouter>
        <Routes>
          <Route path={'/'} element={<Navbar/>}>
            <Route index element={<Placeholder/>}/>
            <Route path={'projects'} element={<Projects
              projects={this.state.projects}
              tasks={this.state.tasks}
              selectFunc={(id) => this.selectProject(id)}
              selectedProject={this.state.selected_project}
            />}/>
            <Route path={'users'} element={<Placeholder/>}/>
            <Route path={'profile'} element={<Placeholder/>}/>
          </Route>
        </Routes>
      </BrowserRouter>}
    </div>);
  }
}

export default App;
