import { Link, useLocation } from "react-router-dom";

function Navbar() {
  const location = useLocation();

  return (
    <header className="flex justify-between items-center my-7">
      <Link to="/">
        <h1 className="text-3xl font-bold">Product App</h1>
      </Link>
      {location.pathname === "/" ? (
        <Link
          to="/products/new"
          className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded"
        >
          Create Product
        </Link>
      ) : (
        <Link
          to="/"
          className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded"
        >
          Back
        </Link>
      )}
    </header>
  );
}

export default Navbar;
