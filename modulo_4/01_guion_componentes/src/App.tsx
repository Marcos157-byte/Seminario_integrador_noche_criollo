// src/App.tsx

import { useAuth }  from './useContext/AuthContext'
import AppHeader    from './useContext/AppHeader'
import LoginForm    from './useContext/LoginForm'
import ThemeToggle  from './useContext/ThemeToggle'
import UserBadge    from './useContext/serBadge'
import PrimeSieve from './useMemo/PrimeSieve'
import FilteredCatalog from './useMemo/FilteredCatalog'
// ┌──────────────────────────────────────────────────────────────────────┐
// │  Cambia PASO y guarda (Ctrl+S) para navegar entre componentes.      │
// │  1  ThemeToggle   — botón que alterna el tema desde el contexto     │
// │  2  UserBadge     — badge de usuario autenticado con logout         │
// │  3  LoginForm     — formulario de login conectado a AuthContext      │
// │  4  AppHeader     — header con dos contextos simultáneos            │
// └──────────────────────────────────────────────────────────────────────┘
const PASO = 6

export default function App() {
  const { state } = useAuth()

  const content =
    PASO === 1 ? <ThemeToggle /> :
    PASO === 2 ? <UserBadge /> :
    PASO === 3 ? <LoginForm /> :
    PASO === 4 ? <AppHeader /> :
    PASO === 5 ? <PrimeSieve/>:
    PASO === 6 ? <FilteredCatalog/>:
    <p style={{ color: '#e00' }}>Paso {PASO}: crea el componente primero</p>

  return (
    <main style={{ maxWidth: 600, margin: '40px auto', fontFamily: 'sans-serif', padding: '0 16px' }}>
      {PASO === 6 ? content : (
        <>
          {state.user && (
            <p style={{ marginBottom: 16, fontSize: 14, color: '#6b7280' }}>
              Sesión activa: <strong>{state.user.name}</strong>
            </p>
          )}
          {content}
        </>
      )}
    </main>
  )
}