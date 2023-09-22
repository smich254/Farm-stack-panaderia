import { useEffect, useState } from "react";
import ProductList from "../components/ProductList";
import { fetchProducts } from "../api/products";

function HomePage() {
  const [simpleProducts, setSimpleProducts] = useState([]);
  const [favoriteProducts, setFavoriteProducts] = useState([]);

  useEffect(() => {
    fetchProducts()
      .then((res) => {
        setSimpleProducts(res.data.filter((product) => product.favorite));
        setFavoriteProducts(res.data.filter((product) => !product.favorite));
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <h3 className="text-xl font-bold text-gray-400 mb-7">Simple Products</h3>
      <ProductList products={simpleProducts} />

      <h3 className="text-xl font-bold text-gray-400 mb-7">
        Favorite Products
      </h3>
      <ProductList products={favoriteProducts} />
    </>
  );
}

export default HomePage;
