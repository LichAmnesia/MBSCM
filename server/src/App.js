/**
* @Author: Lich_Amnesia
* @Date:   2016-11-30T00:26:14-07:00
* @Email:  Shen.Huang@Colorado.Edu
* @Last modified by:   Lich_Amnesia
* @Last modified time: 2016-11-30T00:26:14-07:00
*/



import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';




class App extends Component {


  render() {
    var PythonShell = require('python-shell');
    PythonShell.run('compute_input.py', function (err) {
      if (err) throw err;
      console.log('finished');
    });
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
