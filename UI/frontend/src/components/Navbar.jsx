import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { SidebarData } from './sidebar';
import './Navbar.css';
import { IconContext } from 'react-icons';
import { useLocation } from 'react-router-dom';
function Navbar() {
  const [sidebar, setSidebar] = useState(true);
  const location = useLocation();

  const showSidebar = () => setSidebar(sidebar);

  return (
    <>
      <IconContext.Provider value={{ color: '#fff' }}>
        <div className='navbar'>
          <Link to='#' className='menu-bars'>
            {/* <FaIcons.FaBars onClick={showSidebar} /> */}
            {/* <h5>Nav</h5> */}
          </Link>
        </div>
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
          {/* <h2>Navbar</h2> */}
          <ul className='nav-menu-items' onClick={showSidebar}>
            <li className='navbar-toggle'>
              <Link to='#' className='menu-bars'>
                {/* <AiIcons.AiOutlineClose /> */}
              </Link>
            </li>
            {SidebarData.map((item, index) => {
              const isActive = location.pathname === item.path;
              return (
                <li key={index} className={`nav-text ${isActive ? 'active' : ''}`}>
                  <Link to={item.path}>
                    {/* {item.icon} */}
                    <span>{item.title}</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
      </IconContext.Provider>
          {/* <p>hell0</p> */}
    </>
  );
}

export default Navbar;