import React, { useState, useEffect } from 'react';

export function Shop() {
    const [currentProduct, setCurrentProduct] = useState(0);

    useEffect(() => {
        fetch('/products').then(res => res.json()).then(data => {
            setCurrentProduct(data[0]);
        });
    }, []);

    return (
        <div>
            <p>
                {currentProduct.title}
            </p>
        </div>
    );
}

