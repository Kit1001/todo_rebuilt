import React from "react";
import {NavLink, Outlet} from "react-router-dom";
import Logo from '../svgs/task-svgrepo-com.svg'
import './Navbar.css'

const classNames = require('classnames');

function Navbar(props) {
  return (<div>
      <header className="header">
        <nav className="container">
          <div className="logo">
            <NavLink to={"/"} className="logo-link">
              <img src={Logo} alt="logo" className="logo-svg"/>
            </NavLink>
          </div>
          <nav className="navbar">
            <ul>
              <li><NavLink to="projects" className='link'>Projects & tasks</NavLink></li>
              <li><NavLink to="users" className='link'>Users</NavLink></li>
            </ul>
          </nav>
        </nav>
        <div className="profile">
          <div>
            <NavLink to={'profile'} className="link">
              <img src={'https://kingstonplaza.com/wp-content/uploads/2015/07/generic-avatar-300x300.png'} className={'avatar'} alt={'avatar'}/>
              <span className={'profile_text'}>Admin</span>
            </NavLink>
            </div>
        </div>
      </header>
      <Outlet/>
    </div>
  )
}

export default Navbar