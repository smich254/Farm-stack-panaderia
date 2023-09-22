import ProductCard from "./ProductCard";

function ProductList({ products }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      {products.map((product, i) => {
        return <ProductCard product={product} key={i} />;
      })}
    </div>
  );
}

export default ProductList;
