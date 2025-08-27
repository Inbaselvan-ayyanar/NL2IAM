import React, { useState } from 'react';
import Home from './Components/pages/Home';
import Group from './Components/pages/Group';
import User from './Components/pages/User';

const App = () => {
  const [activeComponent, setActiveComponent] = useState('home');

  return (
    <div>
      <div style={{ display: 'flex', gap: '20px', justifyContent: 'center', margin: '40px 0' }}>
        <button className="primary-button" onClick={() => setActiveComponent('home')}>Home</button>
        <button className="primary-button" onClick={() => setActiveComponent('group')}>IAM Group</button>
        <button className="primary-button" onClick={() => setActiveComponent('user')}>IAM User</button>
      </div>
      <div>
        {activeComponent === 'home' && <Home />}
        {activeComponent === 'group' && <Group />}
        {activeComponent === 'user' && <User />}
      </div>
    </div>
  );
};

export default App;
