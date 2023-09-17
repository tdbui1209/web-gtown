// src/routes/routes.js
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import QuanLyLoaiSanPham from '../views/QuanLyLoaiSanPham';
import QuanLySanPham from '../views/QuanLySanPham';
import QuanLyNguoiDung from '../views/QuanLyNguoiDung';
import DangNhap from '../views/DangNhap';
import DangKy from '../views/DangKy';
const AppRoutes = () => {
  return (
    <Routes>
      <Route path='/' element={<DangNhap />}/>
      <Route path='/dang_nhap' element={<DangNhap />}/>
      <Route path='/dang_ky' element={<DangKy />}/>
      <Route path='/quan_ly_san_pham' element={<QuanLySanPham />}/>
      <Route path='/quan_ly_loai_san_pham' element={<QuanLyLoaiSanPham />} />
      <Route path='/quan_ly_nguoi_dung' element={<QuanLyNguoiDung />} />
    </Routes>
  );
};

export default AppRoutes;
