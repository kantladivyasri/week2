import Dashboard from './pages/Dashboard'
import ConnectionStatus from './components/ConnectionStatus'
import './styles/index.css'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Air Traffic Transcriber & Analyzer</h1>
        <ConnectionStatus />
      </header>
      <main>
        <Dashboard />
      </main>
    </div>
  )
}

export default App

