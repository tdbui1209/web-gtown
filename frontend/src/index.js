import React, { Component } from 'react';
import { BrowserRouter, Routes ,Route } from 'react-router-dom';
import ReactDOM from 'react-dom';
import QuanLySanPham from './views/QuanLySanPham';

class App extends Component{
  render(){
    return (
      <React.StrictMode>
        <BrowserRouter>
          <Routes>
            <Route exact path='/' element={<QuanLySanPham/>}>
            </Route>
          </Routes>
        </BrowserRouter>
      </React.StrictMode>
    );
  }
}
const rootElement = document.getElementById('root');
ReactDOM.render(<App/>, rootElement);