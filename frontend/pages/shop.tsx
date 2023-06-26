'use client'

import { useState, useEffect } from 'react'

export default function Shop() {
    const [currentProduct, setCurrentProduct] = useState(0)
    useEffect(() => {
        fetch('/api/products').then(res => res.json()).then(data => {
            setCurrentProduct(data[0])
        })
    }, [])

    return (
	<main className="flex min-h-screen flex-col items-center justify-between p-24">
            <div>
                <p>{currentProduct.title}</p>
	    </div>
	</main>
    )
}
