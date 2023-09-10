import React from "react";
import Header from "../components/admin/header";
import FormQuanLySanPham from "../components/admin/FormQuanLySanPham";
import TableSanPham from "../components/admin/TableSanPham";

const QuanLySanPham = () =>{
  return(
    <div>
      <Header/>
      <FormQuanLySanPham/>
      <TableSanPham/>
    </div>
  );
}

export default QuanLySanPham;