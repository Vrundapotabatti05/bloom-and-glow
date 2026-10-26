"use client";

import { useState, useMemo } from "react";
import { products, UPI_ID, BANK_DETAILS, type Product } from "@/lib/products";

type CartItem = { name: string; price: number; emoji: string; quantity: number };

type CustomerInfo = {
  first_name?: string;
  last_name?: string;
  phone?: string;
  email?: string;
  pincode?: string;
  address?: string;
  landmark?: string;
  state?: string;
};

type Payment = { method: string; upi_id?: string; reference?: string; amount?: number; bank?: string };

const STATES = ["Select State", "Andhra Pradesh", "Bihar", "Delhi", "Goa", "Gujarat", "Haryana", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Punjab", "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh", "West Bengal"];

function renderStars(rating: number) {
  const full = Math.floor(rating);
  const half = rating - full >= 0.5 ? 1 : 0;
  return "★".repeat(full) + (half ? "½" : "") + "☆".repeat(5 - full - half);
}

function Btn({ children, onClick, primary, full, type }: { children: React.ReactNode; onClick?: () => void; primary?: boolean; full?: boolean; type?: "button" | "submit" }) {
  return (
    <div className="stButton" style={{ width: full ? "100%" : undefined }}>
      <button type={type || "button"} onClick={onClick} style={{ width: full ? "100%" : undefined }}>
        {children}
      </button>
    </div>
  );
}

export default function Home() {
  const [cart, setCart] = useState<CartItem[]>([]);
  const [cartTotal, setCartTotal] = useState(0);
  const [checkoutStep, setCheckoutStep] = useState(0);
  const [customerInfo, setCustomerInfo] = useState<CustomerInfo>({});
  const [selectedPayment, setSelectedPayment] = useState<Payment | null>(null);
  const [orderId, setOrderId] = useState<string | null>(null);
  const [activeCategory, setActiveCategory] = useState<string | null>(null);
  const [viewProduct, setViewProduct] = useState<Product | null>(null);
  const [orderHistory, setOrderHistory] = useState<any[]>([]);
  const [showOrders, setShowOrders] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");

  const cartCount = cart.length;

  const addToCart = (product: Product, quantity = 1) => {
    setCart((prev) => [...prev, { name: product.name, price: product.price, emoji: product.emoji, quantity }]);
    setCartTotal((prev) => prev + product.price * quantity);
  };

  const removeFromCart = (idx: number) => {
    setCart((prev) => {
      const item = prev[idx];
      setCartTotal((t) => t - item.price * item.quantity);
      return prev.filter((_, i) => i !== idx);
    });
  };

  const clearCart = () => {
    setCart([]);
    setCartTotal(0);
  };

  const delivery = cartTotal >= 999 ? 0 : 49;
  const total = cartTotal + delivery;

  // search results
  const searchResults = useMemo(() => {
    if (!searchQuery.trim()) return null;
    const q = searchQuery.toLowerCase();
    const results: Product[] = [];
    for (const items of Object.values(products)) {
      for (const item of items) {
        if (
          item.name.toLowerCase().includes(q) ||
          item.desc.toLowerCase().includes(q) ||
          (item.material || "").toLowerCase().includes(q) ||
          (item.occasion || "").toLowerCase().includes(q)
        ) {
          results.push(item);
        }
      }
    }
    return results;
  }, [searchQuery]);

  // ---- View product detail ----
  if (viewProduct) {
    const product = viewProduct;
    const saved = product.original_price - product.price;
    return (
      <div className="stApp" style={{ minHeight: "100vh", padding: "20px" }}>
        <div style={{ maxWidth: 900, margin: "0 auto" }}>
          <Btn onClick={() => setViewProduct(null)}>← Back to Shop</Btn>
          <div className="product-detail-card" style={{ marginTop: 15 }}>
            <div className="detail-img">{product.emoji}</div>
            <div className="detail-body">
              <div className="detail-name">{product.name}</div>
              <div className="detail-rating">
                <span className="stars" style={{ fontSize: "1.3rem" }}>{renderStars(product.rating || 4.5)}</span>
                <span style={{ color: "#D63384", fontWeight: 700, fontSize: "1.1rem" }}>{product.rating || 4.5}</span>
                <span style={{ color: "#999" }}>({product.reviews || 100} reviews)</span>
              </div>
              <p style={{ color: "#555", fontSize: "1rem", lineHeight: 1.7, marginBottom: 15 }}>{product.desc}</p>
              <div className="detail-price-row">
                <span className="detail-now">Rs.{product.price}</span>
                <span className="detail-was">Rs.{product.original_price}</span>
                <span className="detail-save">You Save Rs.{saved} ({product.discount}% OFF)</span>
              </div>
              <div className="detail-specs">
                <h4 style={{ fontFamily: "'Playfair Display',serif", color: "#D63384", marginBottom: 10 }}>Product Details</h4>
                <div className="spec-row">
                  {Object.entries(product)
                    .filter(([k]) => !["name", "price", "original_price", "discount", "emoji", "desc", "rating", "reviews"].includes(k))
                    .map(([k, v]) => (
                      <span key={k} className="spec-item">{k.charAt(0).toUpperCase() + k.slice(1)}: {String(v)}</span>
                    ))}
                </div>
              </div>
              <div className="detail-features">
                <h4 style={{ fontFamily: "'Playfair Display',serif", color: "#D63384", marginBottom: 10 }}>Highlights</h4>
                {(product.features || ["Premium Quality", "Gift Ready", "Fast Delivery"]).map((f, i) => (
                  <div key={i} className="feat-item"><span className="feat-check">✔</span> {f}</div>
                ))}
              </div>
            </div>
          </div>
          <div style={{ marginTop: 15, display: "flex", justifyContent: "center" }}>
            <div style={{ width: 300 }}>
              <Btn full primary onClick={() => { addToCart(product); alert(`Added ${product.name} to cart!`); setViewProduct(null); }}>
                Add to Cart
              </Btn>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // ---- Checkout steps ----
  if (checkoutStep > 0) {
    return (
      <div className="stApp" style={{ minHeight: "100vh", padding: "20px" }}>
        <div style={{ maxWidth: 1100, margin: "0 auto" }}>
          <div className="main-header" style={{ padding: "15px 40px", marginBottom: 20 }}>
            <h1 style={{ fontSize: "2rem" }}>Bloom & Glow — Checkout</h1>
          </div>
          {/* step indicator */}
          <div className="step-indicator">
            {["Cart", "Details", "Payment", "Confirm"].map((label, idx) => {
              const num = idx + 1;
              const cls = num <= checkoutStep ? "active" : "inactive";
              const lblCls = num <= checkoutStep ? "active" : "";
              return (
                <div key={label} className="step">
                  <div className={`step-circle ${cls}`}>{num}</div>
                  <span className={`step-label ${lblCls}`}>{label}</span>
                </div>
              );
            })}
          </div>

          {checkoutStep === 1 && (
            <CartSection cart={cart} cartTotal={cartTotal} removeFromCart={removeFromCart} clearCart={clearCart} onProceed={() => setCheckoutStep(2)} />
          )}
          {checkoutStep === 2 && (
            <CustomerDetails customerInfo={customerInfo} setCustomerInfo={setCustomerInfo} onBack={() => setCheckoutStep(1)} onContinue={() => setCheckoutStep(3)} />
          )}
          {checkoutStep === 3 && (
            <PaymentOptions
              total={total}
              selectedPayment={selectedPayment}
              setSelectedPayment={setSelectedPayment}
              onBack={() => setCheckoutStep(2)}
              onPlace={(oid: string) => { setOrderId(oid); setCheckoutStep(4); }}
              cart={cart}
              customerInfo={customerInfo}
              cartTotal={cartTotal}
              setOrderHistory={setOrderHistory}
              clearCart={clearCart}
            />
          )}
          {checkoutStep === 4 && (
            <OrderConfirmation
              orderId={orderId}
              customerInfo={customerInfo}
              selectedPayment={selectedPayment}
              cart={cart}
              cartTotal={cartTotal}
              onContinue={() => {
                clearCart();
                setCustomerInfo({});
                setSelectedPayment(null);
                setOrderId(null);
                setCheckoutStep(0);
              }}
            />
          )}
        </div>
      </div>
    );
  }

  // ---- Main shop ----
  return (
    <div className="stApp" style={{ minHeight: "100vh", padding: "20px" }}>
      <div style={{ maxWidth: 1280, margin: "0 auto" }}>
        {/* cart badge */}
        {cartCount > 0 && checkoutStep === 0 && (
          <div className="cart-badge">Cart ({cartCount}) — Rs.{cartTotal}</div>
        )}

        {showOrders ? (
          <>
            <OrderHistory orderHistory={orderHistory} onContinue={() => setShowOrders(false)} />
            <Footer />
          </>
        ) : null}

        {!showOrders && (
          <>
            {/* search bar */}
            <div className="search-wrapper">
              <div style={{ textAlign: "center", marginBottom: 15 }}>
                <h1 style={{ fontFamily: "'Playfair Display',serif", background: "linear-gradient(135deg, #FF69B4 0%, #FF1493 50%, #9370DB 100%)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", backgroundClip: "text", fontSize: "2.8rem", margin: 0 }}>Bloom & Glow</h1>
                <p style={{ color: "#D63384", fontSize: "1rem", margin: "5px 0 0 0", fontWeight: 500 }}>Premium Gifts for Every Special Occasion</p>
              </div>
              <div style={{ display: "flex", justifyContent: "center" }}>
                <div style={{ width: "60%" }}>
                  <div className="stTextInput">
                    <input
                      type="text"
                      placeholder="🔍  Search for candles, flowers, jewelry, beauty products..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      style={{ width: "100%" }}
                    />
                  </div>
                </div>
              </div>
              {orderHistory.length > 0 && (
                <div style={{ display: "flex", justifyContent: "center", marginTop: 10 }}>
                  <div style={{ width: 160 }}>
                    <Btn full onClick={() => setShowOrders(true)}>My Orders</Btn>
                  </div>
                </div>
              )}
              <div className="search-tags">
                <span className="search-tag">🕯️ Candles</span>
                <span className="search-tag">💐 Corset Flowers</span>
                <span className="search-tag">🌸 Bouquets</span>
                <span className="search-tag">💍 Jewelry</span>
                <span className="search-tag">💄 Beauty</span>
                <span className="search-tag">🧸 Soft Toys</span>
              </div>
            </div>

            <OfferBanner />
            <Categories activeCategory={activeCategory} setActiveCategory={setActiveCategory} />

            {searchResults ? (
              <>
                <h2 className="section-header">Search Results for &quot;{searchQuery}&quot;</h2>
                {searchResults.length > 0 ? (
                  <ProductGrid products={searchResults} onView={setViewProduct} onAdd={addToCart} />
                ) : (
                  <div style={{ padding: 20, textAlign: "center", color: "#D63384" }}>No products found. Try a different search term.</div>
                )}
              </>
            ) : activeCategory ? (
              <>
                <h2 className="section-header">{activeCategory}</h2>
                <ProductGrid products={products[activeCategory]} onView={setViewProduct} onAdd={addToCart} />
              </>
            ) : (
              Object.entries(products).map(([cat, items]) => (
                <div key={cat}>
                  <h2 className="section-header">Featured {cat}</h2>
                  <ProductGrid products={items} onView={setViewProduct} onAdd={addToCart} />
                </div>
              ))
            )}

            <Features />
            <Footer />

            {cart.length > 0 && (
              <>
                <div className="divider" />
                <CartSection cart={cart} cartTotal={cartTotal} removeFromCart={removeFromCart} clearCart={clearCart} onProceed={() => setCheckoutStep(1)} showCheckoutBtn />
              </>
            )}
          </>
        )}
      </div>
    </div>
  );
}

function OfferBanner() {
  return (
    <div className="offer-banner">
      SPECIAL OFFER: Use code BLOOM30 for extra 30% off on your first order! | Free delivery on orders above Rs.999
    </div>
  );
}

function Categories({ activeCategory, setActiveCategory }: { activeCategory: string | null; setActiveCategory: (c: string | null) => void }) {
  const cats = Object.keys(products);
  const icons = ["🕯️", "💐", "🌸", "💍", "💄", "🧸"];
  return (
    <>
      <h2 className="section-header">Shop by Category</h2>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(6, 1fr)", gap: 12 }}>
        {cats.map((cat, idx) => {
          const isActive = activeCategory === cat;
          return (
            <div
              key={cat}
              className={`category-btn ${isActive ? "active" : ""}`}
              onClick={() => setActiveCategory(activeCategory === cat ? null : cat)}
              style={{ cursor: "pointer" }}
            >
              <div className="cat-icon">{icons[idx]}</div>
              <div className="cat-name">{cat}</div>
            </div>
          );
        })}
      </div>
    </>
  );
}

function ProductGrid({ products: items, onView, onAdd }: { products: Product[]; onView: (p: Product) => void; onAdd: (p: Product) => void }) {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 16, marginTop: 10 }}>
      {items.map((product) => {
        const saved = product.original_price - product.price;
        return (
          <div key={product.name} className="product-card">
            <div className="product-img">
              {product.emoji}
              <div className="product-badge">{product.discount}% OFF</div>
              <div className="product-wishlist">♡</div>
            </div>
            <div className="product-body">
              <div className="product-name">{product.name}</div>
              <div className="product-desc">{product.desc.slice(0, 80)}...</div>
              <div className="product-rating">
                <span className="stars">{renderStars(product.rating || 4.5)}</span>
                <span style={{ color: "#D63384", fontWeight: 600 }}>{product.rating || 4.5}</span>
                <span className="rating-count">({product.reviews || 100})</span>
              </div>
              <div className="product-tags">
                <span className="ptag">{(product.material || "Premium").slice(0, 20)}</span>
                <span className="ptag">{(product.occasion || "Gifting").slice(0, 20)}</span>
              </div>
              <div className="product-price-row">
                <span className="price-now">Rs.{product.price}</span>
                <span className="price-was">Rs.{product.original_price}</span>
                <span className="price-save">Save Rs.{saved}</span>
              </div>
            </div>
            <div style={{ padding: "0 18px 18px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
              <Btn full onClick={() => onView(product)}>View Details</Btn>
              <Btn full onClick={() => onAdd(product)}>Add to Cart</Btn>
            </div>
          </div>
        );
      })}
    </div>
  );
}

function Features() {
  const features = [
    ["🚚", "Free Delivery", "Free shipping on orders above Rs.999"],
    ["🎁", "Gift Wrapping", "Beautiful premium gift wrapping included"],
    ["🔒", "Secure Payment", "100% secure payment options"],
    ["💝", "Special Offers", "Exclusive discounts every week"],
  ];
  return (
    <>
      <div className="divider" />
      <h2 className="section-header">Why Choose Us</h2>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 }}>
        {features.map(([icon, title, desc]) => (
          <div key={title} className="feature-box">
            <div className="feature-icon">{icon}</div>
            <div className="feature-title">{title}</div>
            <div className="feature-desc">{desc}</div>
          </div>
        ))}
      </div>
    </>
  );
}

function Footer() {
  return (
    <div className="footer">
      <h3>Bloom & Glow</h3>
      <p>Making every moment special with our curated collection of premium gifts.</p>
      <p style={{ marginTop: 20, fontSize: "0.9rem" }}>Contact: support@bloomandglow.com | +91 98765 43210</p>
      <p style={{ fontSize: "0.85rem", marginTop: 10 }}>© 2026 Bloom & Glow. All rights reserved.</p>
    </div>
  );
}

function CartSection({ cart, cartTotal, removeFromCart, clearCart, onProceed, showCheckoutBtn }: any) {
  const delivery = cartTotal >= 999 ? 0 : 49;
  const total = cartTotal + delivery;
  if (!cart.length) {
    return <div style={{ padding: 20, color: "#D63384" }}>Your cart is empty. Start shopping to add items!</div>;
  }
  return (
    <div>
      <h2 className="section-header">Your Cart ({cart.length} items)</h2>
      {cart.map((item: CartItem, idx: number) => (
        <div key={idx} style={{ display: "grid", gridTemplateColumns: "3fr 2fr 1fr 1fr", gap: 8, alignItems: "center", padding: "8px 0", borderBottom: "1px solid #FFE4E1" }}>
          <div>{item.emoji} <strong>{item.name}</strong></div>
          <div>Rs.{item.price} x {item.quantity}</div>
          <div><strong>Rs.{item.price * item.quantity}</strong></div>
          <div style={{ width: 100 }}>
            <Btn full onClick={() => removeFromCart(idx)}>Remove</Btn>
          </div>
        </div>
      ))}
      <div className="divider" />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        <div>
          <h3>Subtotal: Rs.{cartTotal}</h3>
          {cartTotal >= 999 ? <div style={{ color: "green" }}>You qualify for FREE delivery!</div> : <div style={{ color: "#D63384" }}>Add Rs.{999 - cartTotal} more for free delivery</div>}
        </div>
        <div>
          <h3>Delivery: {delivery === 0 ? "FREE" : "Rs.49"}</h3>
        </div>
      </div>
      <h3>Total Amount: <strong>Rs.{total}</strong></h3>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginTop: 12 }}>
        <Btn full primary onClick={onProceed}>Proceed to Checkout</Btn>
        <Btn full onClick={clearCart}>Clear Cart</Btn>
      </div>
    </div>
  );
}

function CustomerDetails({ customerInfo, setCustomerInfo, onBack, onContinue }: any) {
  const [first, setFirst] = useState(customerInfo.first_name || "");
  const [last, setLast] = useState(customerInfo.last_name || "");
  const [phone, setPhone] = useState(customerInfo.phone || "");
  const [email, setEmail] = useState(customerInfo.email || "");
  const [pincode, setPincode] = useState(customerInfo.pincode || "");
  const [address, setAddress] = useState(customerInfo.address || "");
  const [landmark, setLandmark] = useState(customerInfo.landmark || "");
  const [state, setState] = useState(customerInfo.state || "Select State");

  const handleContinue = () => {
    if (first && last && phone && pincode && address && state !== "Select State") {
      setCustomerInfo({ first_name: first, last_name: last, phone, email, pincode, address, landmark, state });
      onContinue();
    } else {
      alert("Please fill all required fields (*)");
    }
  };

  return (
    <div>
      <h2 className="section-header">Delivery Details</h2>
      <div style={{ background: "linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 50%, #F8F0FF 100%)", borderRadius: 20, padding: 30, border: "2px solid #FF69B4", marginBottom: 25, boxShadow: "0 5px 20px rgba(255,20,147,0.15)" }}>
        <div style={{ textAlign: "center", marginBottom: 20 }}>
          <span style={{ fontSize: "2.5rem" }}>📦</span>
          <h3 style={{ fontFamily: "'Playfair Display',serif", background: "linear-gradient(135deg, #FF1493 0%, #9370DB 100%)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", backgroundClip: "text", margin: "10px 0 5px 0", fontSize: "1.4rem" }}>Where should we deliver your gifts?</h3>
          <p style={{ color: "#D63384", fontSize: "0.9rem" }}>All fields with * are required</p>
        </div>
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
        <div className="stTextInput"><label>👤 First Name *</label><input value={first} onChange={(e) => setFirst(e.target.value)} /></div>
        <div className="stTextInput"><label>👤 Last Name *</label><input value={last} onChange={(e) => setLast(e.target.value)} /></div>
        <div className="stTextInput"><label>📱 Phone Number *</label><input value={phone} onChange={(e) => setPhone(e.target.value)} maxLength={10} /></div>
        <div className="stTextInput"><label>✉️ Email Address</label><input value={email} onChange={(e) => setEmail(e.target.value)} /></div>
        <div className="stSelectbox">
          <label>📍 State *</label>
          <select value={state} onChange={(e) => setState(e.target.value)} style={{ width: "100%", padding: 10, borderRadius: 15, border: "2px solid #FF69B4" }}>
            {STATES.map((s) => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
        <div className="stTextInput"><label>📮 Pincode *</label><input value={pincode} onChange={(e) => setPincode(e.target.value)} maxLength={6} /></div>
      </div>
      <div className="stTextArea" style={{ marginTop: 12 }}>
        <label>🏠 Full Delivery Address *</label>
        <textarea value={address} onChange={(e) => setAddress(e.target.value)} rows={4} style={{ width: "100%" }} />
      </div>
      <div className="stTextInput" style={{ marginTop: 12 }}>
        <label>🗺️ Landmark (Optional)</label>
        <input value={landmark} onChange={(e) => setLandmark(e.target.value)} />
      </div>
      <div className="divider" />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
        <Btn full onClick={onBack}>Back to Cart</Btn>
        <Btn full primary onClick={handleContinue}>Continue to Payment</Btn>
      </div>
    </div>
  );
}

function PaymentOptions({ total, selectedPayment, setSelectedPayment, onBack, onPlace, cart, customerInfo, cartTotal, setOrderHistory, clearCart }: any) {
  const [method, setMethod] = useState("UPI Payment");
  const [upiRef, setUpiRef] = useState(selectedPayment?.reference || "");
  const [bankRef, setBankRef] = useState(selectedPayment?.reference || "");

  const handlePlace = () => {
    let payment = selectedPayment;
    // sync refs
    if (method === "UPI Payment") {
      if (!upiRef) { alert("Please enter the transaction reference number!"); return; }
      payment = { method: "UPI", upi_id: UPI_ID, reference: upiRef, amount: total };
    } else if (method === "Bank Transfer") {
      if (!bankRef) { alert("Please enter the transaction reference number!"); return; }
      payment = { method: "Bank Transfer", bank: BANK_DETAILS.bank_name, reference: bankRef, amount: total };
    } else {
      payment = { method: "COD", amount: total };
    }
    if (!payment) { alert("Please select a payment method!"); return; }
    if ((payment.method === "UPI" || payment.method === "Bank Transfer") && !payment.reference) {
      alert("Please enter the transaction reference number!");
      return;
    }
    const oid = `BG${new Date().toISOString().slice(0, 10).replace(/-/g, "")}${Math.random().toString(36).slice(2, 8).toUpperCase()}`;
    const order = {
      order_id: oid,
      date: new Date().toLocaleString("en-IN", { day: "2-digit", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" }),
      items: cart.map((c: CartItem) => ({ ...c })),
      total,
      payment: { ...payment },
      address: { ...customerInfo },
      status: "Confirmed",
    };
    setOrderHistory((prev: any[]) => [order, ...prev]);
    setSelectedPayment(payment);
    onPlace(oid);
  };

  return (
    <div>
      <h2 className="section-header">Select Payment Method</h2>
      <p><strong>Order Total: Rs.{total}</strong></p>
      <hr />
      <div style={{ display: "flex", gap: 15, marginBottom: 15 }}>
        {["UPI Payment", "Bank Transfer", "Cash on Delivery"].map((m) => (
          <label key={m} style={{ background: "linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 100%)", padding: "12px 20px", borderRadius: 15, border: "2px solid #FFB6C1", cursor: "pointer" }}>
            <input type="radio" name="pm" value={m} checked={method === m} onChange={() => setMethod(m)} style={{ marginRight: 8 }} />
            {m}
          </label>
        ))}
      </div>

      {method === "UPI Payment" && (
        <div>
          <div style={{ background: "linear-gradient(145deg,#FFF5F8,#F8F0FF)", borderRadius: 20, padding: 30, border: "2px solid #FF69B4", marginBottom: 20, textAlign: "center" }}>
            <div style={{ fontSize: "3rem", marginBottom: 10 }}>📱</div>
            <div style={{ fontFamily: "'Playfair Display',serif", fontSize: "1.3rem", fontWeight: 600, color: "#D63384" }}>UPI Payment</div>
            <div style={{ color: "#666", fontSize: "0.95rem" }}>Pay instantly using any UPI app</div>
          </div>
          <div className="upi-id-display">
            <div className="upi-label">Send payment to UPI ID</div>
            <div className="upi-id">{UPI_ID}</div>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 10, marginBottom: 15 }}>
            {[["Google Pay", "💳"], ["PhonePe", "📱"], ["Paytm", "💰"], ["BHIM", "🏦"]].map(([name, icon]) => (
              <div key={name} style={{ textAlign: "center", padding: 15, background: "white", borderRadius: 15, boxShadow: "0 3px 10px rgba(0,0,0,0.08)" }}>
                <div style={{ fontSize: "2.5rem" }}>{icon}</div>
                <div style={{ fontWeight: 600, color: "#333", fontSize: "0.85rem" }}>{name}</div>
              </div>
            ))}
          </div>
          <p><strong>How to pay:</strong></p>
          <p>1. Open your UPI app<br />2. Send <strong>Rs.{total}</strong> to <strong>{UPI_ID}</strong><br />3. Enter transaction ID below</p>
          <div className="stTextInput">
            <label>UPI Reference / Transaction ID *</label>
            <input value={upiRef} onChange={(e) => setUpiRef(e.target.value)} placeholder="e.g., 123456789012" />
          </div>
        </div>
      )}

      {method === "Bank Transfer" && (
        <div>
          <div style={{ background: "linear-gradient(145deg,#FFF5F8,#F8F0FF)", borderRadius: 20, padding: 30, border: "2px solid #FF69B4", marginBottom: 20, textAlign: "center" }}>
            <div style={{ fontSize: "3rem", marginBottom: 10 }}>🏦</div>
            <div style={{ fontFamily: "'Playfair Display',serif", fontSize: "1.3rem", fontWeight: 600, color: "#D63384" }}>Bank Transfer / NEFT / IMPS</div>
            <div style={{ color: "#666", fontSize: "0.95rem" }}>Transfer directly to our bank account</div>
          </div>
          <div className="bank-details">
            <h4>Bank Account Details</h4>
            <p><span className="label">Bank Name:</span> <span className="value">{BANK_DETAILS.bank_name}</span></p>
            <p><span className="label">Account Holder:</span> <span className="value">{BANK_DETAILS.account_name}</span></p>
            <p><span className="label">Account Number:</span> <span className="value">{BANK_DETAILS.account_number}</span></p>
            <p><span className="label">IFSC Code:</span> <span className="value">{BANK_DETAILS.ifsc}</span></p>
            <p><span className="label">Branch:</span> <span className="value">{BANK_DETAILS.branch}</span></p>
            <p><span className="label">Account Type:</span> <span className="value">{BANK_DETAILS.account_type}</span></p>
          </div>
          <p><strong>Transfer Amount: Rs.{total}</strong></p>
          <div className="stTextInput">
            <label>Transaction Reference Number *</label>
            <input value={bankRef} onChange={(e) => setBankRef(e.target.value)} placeholder="e.g., NEFT/IMPS/UPI reference" />
          </div>
        </div>
      )}

      {method === "Cash on Delivery" && (
        <div>
          <div style={{ background: "linear-gradient(145deg,#FFF5F8,#F8F0FF)", borderRadius: 20, padding: 30, border: "2px solid #FF69B4", marginBottom: 20, textAlign: "center" }}>
            <div style={{ fontSize: "3rem", marginBottom: 10 }}>💵</div>
            <div style={{ fontFamily: "'Playfair Display',serif", fontSize: "1.3rem", fontWeight: 600, color: "#D63384" }}>Cash on Delivery</div>
            <div style={{ color: "#666", fontSize: "0.95rem" }}>Pay when your order arrives</div>
          </div>
          {total > 5000 ? (
            <div style={{ color: "orange" }}>COD not available for orders above Rs.5000. Please choose UPI or Bank Transfer.</div>
          ) : (
            <div style={{ color: "#D63384" }}>Please keep <strong>Rs.{total}</strong> ready in cash at delivery.</div>
          )}
        </div>
      )}

      <div className="divider" />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
        <Btn full onClick={onBack}>Back to Details</Btn>
        <Btn full primary onClick={handlePlace}>Place Order</Btn>
      </div>
    </div>
  );
}

function OrderConfirmation({ orderId, customerInfo, selectedPayment, cart, cartTotal, onContinue }: any) {
  const delivery = cartTotal >= 999 ? 0 : 49;
  const total = cartTotal + delivery;
  return (
    <div>
      <div className="order-success">
        <h2>Order Placed Successfully!</h2>
        <p>Thank you for shopping with Bloom & Glow!</p>
        <div className="order-id">Order ID: {orderId}</div>
      </div>
      <hr />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        <div>
          <h3>Delivery Details</h3>
          <p><strong>Name:</strong> {customerInfo.first_name} {customerInfo.last_name}</p>
          <p><strong>Phone:</strong> {customerInfo.phone}</p>
          {customerInfo.email && <p><strong>Email:</strong> {customerInfo.email}</p>}
          <p><strong>Address:</strong> {customerInfo.address}</p>
          {customerInfo.landmark && <p><strong>Landmark:</strong> {customerInfo.landmark}</p>}
          <p><strong>Pincode:</strong> {customerInfo.pincode} | <strong>State:</strong> {customerInfo.state}</p>
        </div>
        <div>
          <h3>Payment Details</h3>
          <p><strong>Method:</strong> {selectedPayment?.method} | <strong>Amount:</strong> Rs.{selectedPayment?.amount}</p>
          {selectedPayment?.reference && <p><strong>Reference:</strong> {selectedPayment.reference}</p>}
          <h3>Order Items</h3>
          {cart.map((item: CartItem, i: number) => (
            <p key={i}>{item.emoji} {item.name} x {item.quantity} — Rs.{item.price * item.quantity}</p>
          ))}
        </div>
      </div>
      <div className="divider" />
      <div style={{ background: "#FFF0F5", padding: 15, borderRadius: 12 }}>
        <strong>What happens next?</strong>
        <p>1. Order confirmation on phone/email<br />2. Processing within 24 hours<br />3. Delivery in 3-5 business days<br />4. Queries: support@bloomandglow.com | +91 98765 43210</p>
      </div>
      <div style={{ marginTop: 15 }}>
        <Btn full primary onClick={onContinue}>Continue Shopping</Btn>
      </div>
    </div>
  );
}

function OrderHistory({ orderHistory, onContinue }: any) {
  const statusColors: Record<string, string> = { Confirmed: "#4CAF50", Processing: "#FF9800", Shipped: "#2196F3", Delivered: "#9C27B0" };
  return (
    <div>
      <h2 className="section-header">My Orders</h2>
      {orderHistory.length === 0 ? (
        <div style={{ padding: 20, color: "#D63384" }}>You haven&apos;t placed any orders yet. Start shopping!</div>
      ) : (
        orderHistory.map((order: any) => (
          <div key={order.order_id} style={{ background: "white", borderRadius: 20, padding: 25, marginBottom: 20, boxShadow: "0 5px 20px rgba(255,20,147,0.1)", border: "2px solid #FFB6C1" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 10, marginBottom: 15 }}>
              <div>
                <span style={{ fontFamily: "'Playfair Display',serif", fontSize: "1.2rem", fontWeight: 700, color: "#FF1493" }}>Order #{order.order_id}</span>
                <span style={{ color: "#888", marginLeft: 15, fontSize: "0.9rem" }}>📅 {order.date}</span>
              </div>
              <span style={{ background: statusColors[order.status] || "#4CAF50", color: "white", padding: "6px 18px", borderRadius: 20, fontWeight: 600, fontSize: "0.85rem" }}>✓ {order.status}</span>
            </div>
            <div style={{ background: "#FFF0F5", borderRadius: 12, padding: 15, marginBottom: 15 }}>
              {order.items.map((item: CartItem, i: number) => (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: 12, padding: "10px 0", borderBottom: "1px solid #FFE4E1" }}>
                  <span style={{ fontSize: "1.8rem" }}>{item.emoji}</span>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontWeight: 600, color: "#333" }}>{item.name}</div>
                    <div style={{ color: "#888", fontSize: "0.85rem" }}>Qty: {item.quantity}</div>
                  </div>
                  <div style={{ fontWeight: 700, color: "#FF1493" }}>Rs.{item.price * item.quantity}</div>
                </div>
              ))}
            </div>
            <div style={{ display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 15 }}>
              <div style={{ color: "#555", fontSize: "0.9rem" }}>
                <strong>📍 Delivery:</strong> {order.address?.address || "N/A"}, {order.address?.state || "N/A"} - {order.address?.pincode || "N/A"}
              </div>
              <div style={{ textAlign: "right" }}>
                <span style={{ color: "#888", fontSize: "0.9rem" }}>Payment: {order.payment?.method}</span><br />
                <span style={{ fontFamily: "'Playfair Display',serif", fontSize: "1.4rem", fontWeight: 700, background: "linear-gradient(135deg, #FF1493 0%, #9370DB 100%)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", backgroundClip: "text" }}>Total: Rs.{order.total}</span>
              </div>
            </div>
          </div>
        ))
      )}
      <div style={{ marginTop: 15 }}>
        <Btn full primary onClick={onContinue}>Continue Shopping</Btn>
      </div>
    </div>
  );
}
