import React, { useState } from "react";
import axios from 'axios';
import '../css/admin/color.css';
import '../css/admin/style.css';
const FormQuanLyLoaiSanPham = () => {
  const url = "http://42.117.108.99:5000/products/categories";
  const[categories, setCategories] = useState({
    product_category_name: ''
  })
  function handleInput(e){
    const newCategories = {...categories};
    newCategories[e.target.id] = e.target.value;
    setCategories(newCategories);
    console.log(newCategories);
  }
  function Submit(e){
    e.preventDefault();
    axios.post(url,{
      product_category_name: categories.product_category_name
    })
    .then(res=>{
      console.log(res.data);
    })
  }
  return(
    <main className="main_admin_site">
      <div className="col-md-12 px-3 py-2">
        <h2 className="font-weight-bold">Overview</h2>
      </div>
      <div className="col-md-12 px-3 py-2">
        <h4 className="title">Quản lý loại sản phẩm</h4>
      </div>
      <form onSubmit={Submit}>
        <div className="col-md-6 p-3">
          <div className="form-group">
            Tên loại sản phẩm
            <input 
              type="text" 
              className="form-control" 
              name="product_category_name" 
              id="product_category_name" 
              value={categories.product_category_name} 
              onChange={handleInput}
            />
          </div>
        </div>
        <div className="col-md-12 py-2">
          <div className="form-group">
            <button onClick={handleInput} type="submit" className="btn font-weight-bold ml-2 button_admin">Thêm loại sản phẩm <i className="bi bi-plus-circle-fill"></i></button>       
          </div>        
        </div>	
      </form>
    </main>
  );
}
export default FormQuanLyLoaiSanPham;