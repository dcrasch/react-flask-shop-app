import NavigationBar from "../components/NavigationBar"
import Footer from "../components/Footer"

import "../styles/globals.css"

export default function MyApp({ Component, pageProps }) {
  return (
    <div className="flex flex-col min-h-screen justify-between">
      <NavigationBar />
      <Component {...pageProps} />
      <Footer />
    </div>
  )
}