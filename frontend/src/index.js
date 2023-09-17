import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import AdminAppRoutes from './routes/admin_routes';
// import Navbar from './components/admin/Navbar';
const App = () => {
  return (
    <React.StrictMode>
      <BrowserRouter>
        {/* <Navbar/> */}
        <AdminAppRoutes />
      </BrowserRouter>
    </React.StrictMode>
  );
};

const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
