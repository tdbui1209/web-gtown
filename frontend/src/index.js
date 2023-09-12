import React, { Component } from 'react';
import { BrowserRouter, Routes ,Route } from 'react-router-dom';
import ReactDOM from 'react-dom';
import QuanLyLoaiSanPham from './views/QuanLyLoaiSanPham';

class App extends Component{
  render(){
    return (
      <React.StrictMode>
        <BrowserRouter>
          <Routes>
            <Route exact path='/'></Route>
            <Route path='/quan_ly_loai_san_pham' element={<QuanLyLoaiSanPham/>}></Route>
          </Routes>
        </BrowserRouter>
      </React.StrictMode>
    );
  }
}
const rootElement = document.getElementById('root');
ReactDOM.render(<App/>, rootElement);