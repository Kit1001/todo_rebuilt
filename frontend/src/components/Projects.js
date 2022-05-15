import React from "react";
import './Projects.css'

const classNames = require('classnames');


const ProjectDetailed = (props) => {
  const project = props.project;
  const expanded = props.selectedProject === project.id;
  const liClassNames = classNames({
    expanded,
  })
  const selectFunc = expanded ? () => props.selectFunc(0) : () => props.selectFunc(project.id);

  return (<li onClick={selectFunc} className={liClassNames}>
    <span>{project.name}</span>
    <table>
      <tbody>
      <tr>
        <td>
          Description:
        </td>
        <td>
          {project.description}
        </td>
      </tr>
      <tr>
        <td>
          Link:
        </td>
        <td>
          <a href={project.link}>{project.link}</a>
        </td>
      </tr>
      </tbody>
    </table>
  </li>)
}

const Task = (props) => {
  const task = props.task;
  const projects = props.projects;
  const project = projects.find((item) => {
    return item.id === task.project
  });
  return (<li className={'task'}>
    <h3>{task.name}</h3>
    {/*<p>Project: <a href={project.link}>{project.name}</a></p>*/}
    <p>{task.description}</p>

  </li>)
}


const Projects = (props) => {
  const projects = props.projects;
  const tasks = props.tasks.filter((el) => el.project === props.selectedProject);
  return (<main>
      <div className={'projects'}>
        <ul className={'projects-list'}>
          {projects && projects.map((item) => <ProjectDetailed
            project={item}
            key={Math.random()}
            selectFunc={(id) => props.selectFunc(id)}
            selectedProject={props.selectedProject}
          />)}
        </ul>
      </div>

      <div className={'tasks'}>
        <ul className={'tasks-list'}>
          {projects && tasks && tasks.map((task) => <Task
            task={task}
            projects={projects}
            key={Math.random()}
          />)}
        </ul>
      </div>
    </main>

  )
}

export default Projects
